from odoo import models, fields, api
from odoo import exceptions

import logging
_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _description = 'To-do Mass Assignment'
    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline = fields.Date('Set Deadline')
    new_user_id = fields.Many2one('res.users', string='Set Responsible')

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not self.new_deadline and not self.new_user_id:
            raise exceptions.ValidationError('No data to update!')
        _logger.debug('Mass update on Todo Tasks %s' % self.task_ids)
        # Values to Write
        vals = {}
        if self.new_deadline:
            vals['date_deadline'] = self.new_deadline
        if self.new_user_id:
            vals['user_id'] = self.new_user_id
        # Mass write values on all selected tasks
        if vals:
            self.task_ids.write(vals)
        return True

    @api.multi
    def do_count_tasks(self):
        Task = self.env['todo.task']
        count = Task.search_count([('is_done', '=', False)])
        raise exceptions.Warning('Counted %d to-do tasks.' % count)

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_populate_tasks(self):
        import pudb; pudb.set_trace()
        self.ensure_one()
        Task = self.env['todo.task']
        open_tasks = Task.search([('is_done', '=', False)])
        self.task_ids = open_tasks
        # reopen wizard form on same wizard record
        return self._reopen_form()
