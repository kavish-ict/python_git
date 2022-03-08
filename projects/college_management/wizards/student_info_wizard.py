# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2one

'''
created wizard for college_management module 
model type : TransientModel 
class name : student.data.wizard
'''

class StudentWizard(models.TransientModel):
    _name = 'student.data.wizard'


    name = fields.Char()
    # syllabus_id = fields.Selection([('option1', 'One'), ('option2', 'Two')], 'syllabus_id')
    my_field = fields.Selection([('option1','male'), ('option', 'female')],string="Gender")
    email_id = fields.Char(string="Email")
    test_ids = fields.Many2many('hr.employee', string='test')
    user_ids = fields.Many2many('res.country', string='Users')
    user_signature = fields.Binary(string='Signature')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def sample_btn(self):
        '''
        sample function created for button
        :return: string
        '''
        print("function works")

    # def cancel_button(self):
    #     print("works")
