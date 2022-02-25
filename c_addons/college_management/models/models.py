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
    branch_id = fields.Selection([('option1', 'Information Technology'), ('option2', 'Computer'),('option3', 'Civil'),('option4', 'Mechanical')],tracking=True)
    my_field = fields.Selection([('option1', 'male'), ('option', 'female')], string="Gender")


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]


    def create_record(self):

        self.create({
            "name": "jake",
            "email_id":"jake@gmail.com",
            "url_id":"instagram.com",
            "my_field":"option1",
            "branch_id":"option3",
            "priority":"4"
        })

    def delete_record(self):
        self.unlink()

    def update_record(self):
        self.write({
            "name": "kavish",
            "email_id": "kavish@gmail.com",
            "url_id": "odoo.com",
            "my_field": "option1",
            "branch_id": "option1",
            "priority": "1"
        })

