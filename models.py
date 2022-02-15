# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2one


class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    relational_id = fields.Many2one('res.partner',string="relation")
    color = fields.Integer()
    resume_id = fields.Binary(string="Resume")
    gender_id = fields.Boolean(string="Male")
    user_signature = fields.Binary(string='Signature')
    rating_avg = fields.Float("Rating Average")

    # syllabus_id = fields.Selection([('option1', 'One'), ('option2', 'Two')], 'syllabus_id')
    my_field = fields.Selection([('option1','male'), ('option', 'female')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


    def sample_btn(self):
        print("function works")
