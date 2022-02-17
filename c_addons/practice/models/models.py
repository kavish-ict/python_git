# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class College(models.Model):
    _name = 'practice.practice'
    _description = 'practice.practice'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    my_selection_field = fields.Selection([('option1','None'),('option2', 'Label 1'), ('option3', 'Label 2')], string='My Selection Field',default='option1')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
