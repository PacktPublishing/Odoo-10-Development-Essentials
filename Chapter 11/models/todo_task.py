# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _inherit = 'todo.task'

    @api.model
    def website_form_input_filter(self, request, values):
        if 'name' in values:
            values['name'] = values['name'].strip()
            if len(values['name']) < 3:
                raise ValidationError(
                    'Text must be at least 3 characters long')
        return values
