# -*- coding: utf-8 -*-

from odoo import models, fields, api


'''
class created for college_management module
class name : college_management.college_management
 
'''
class college_management(models.Model):
    _name = 'college_management.college_management'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'college management module create'

    name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)

    # depart_id = fields.Many2one('res.partner', string="Department")
    state_id = fields.Selection([('pending', 'pending'), ('ongoing', 'ongoing'), ('completed', 'completed')],string="state_id")
    # color = fields.Integer()
    photo_id = fields.Binary(string="Upload your photo")
    progress_bar = fields.Integer(string="progressbar")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Good'), ('2', 'Very Good'), ('3', 'Excellent'),('4','best')],
                                "Appreciation")
    email_id = fields.Char(string="Email")
    test_ids = fields.Many2many('hr.employee',string='test')
    user_ids = fields.Many2many('res.country', string='Users')
    user_signature = fields.Binary(string='Signature')
    # rating_avg = fields.Float("Rating Average")
    # image_id = fields.Binary(string='Image')
    url_id = fields.Char(string='URL')
    branch_id = fields.Selection([('option1', 'Information Technology'), ('option2', 'Computer'),('option3', 'Civil'),('option4', 'Mechanical')])
    my_field = fields.Selection([('option1', 'male'), ('option', 'female')], string="Gender")


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
