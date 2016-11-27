# -*- coding: utf-8 -*-

from datetime import date
from odoo.tests.common import TransactionCase
from odoo.exceptions import Warning
from odoo import fields


class TestWizard(TransactionCase):

    def setUp(self, *args, **kwargs):
        "Setup data"
        super(TestWizard, self).setUp(*args, **kwargs)
        # Setup no pending Todos
        self.env['todo.task']\
            .search([('is_done', '=', False)])\
            .write({'is_done': True})
        # user_demo used to run tests under ACLs
        demo_user = self.env.ref('base.user_demo')
        Todo = self.env['todo.task'].sudo(demo_user)
        Wizard = self.env['todo.wizard'].sudo(demo_user)

        # Setup test Todos
        t0 = date.today()
        self.todo1 = Todo.create({
            'name': 'Todo1',
            'date_deadline': fields.Date.to_string(t0)})
        self.todo2 = Todo.create({
            'name': 'Todo2'})
        # Create test wizard
        self.wizard = Wizard.create({})

    def test_count(self):
        "Test count button"
        with self.assertRaises(Warning) as exc:
            self.wizard.do_count_tasks()
        self.assertIn(' 2 ', str(exc.exception))

    def test_populate_tasks(self):
        "Populate tasks buttons should add two tasks"
        self.wizard.do_populate_tasks()
        count = len(self.wizard.task_ids)
        self.assertEqual(count, 2, 'Wrong number of populated tasks')

    def test_mass_change(self):
        "Mass change deadline date"
        self.wizard.do_populate_tasks()
        self.wizard.new_deadline = self.todo1.date_deadline
        self.wizard.do_mass_update()
        self.assertEqual(self.todo1.date_deadline, self.todo2.date_deadline)
