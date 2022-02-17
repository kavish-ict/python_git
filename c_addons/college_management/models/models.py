# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2one


class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)

    depart_id = fields.Many2one('hr.department', string="Department")
    state_id = fields.Selection([('pending', 'pending'), ('ongoing', 'ongoing'), ('completed', 'completed')],string="state_id")
    color = fields.Integer()
    resume_id = fields.Binary(string="Resume")
    progress_bar = fields.Integer(string="progressbar")
    priority = fields.Selection([('1', 'Normal'), ('2', 'Good'), ('3', 'Very Good'), ('4', 'Excellent'),('5','best'),('7','besvgfgt'),('8','besttt')],
                                "Appreciation")
    email_id = fields.Char(string="Email")
    user_signature = fields.Binary(string='Signature')
    rating_avg = fields.Float("Rating Average")
    image_id = fields.Binary(string='Image')
    url_id = fields.Char(string='URL')
    syllabus_id = fields.Selection([('option1', 'One'), ('option2', 'Two')])
    my_field = fields.Selection([('option1', 'male'), ('option', 'female')], string="Gender")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def sample_btn(self):
        print("function works")
