from odoo import models, fields


class TodoTask(models.Model):
    _inherit = 'todo.task'
    amount_cost = fields.Monetary(
            'Cost',
            currency_field ='currency_id')
    currency_id = fields.Many2one('res.currency')
