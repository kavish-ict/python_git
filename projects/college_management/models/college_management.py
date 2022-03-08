"""new module created"""
from odoo import models, fields, api


class CollegeManagement(models.Model):
    """
    class created with inherited model
    fields type used:Integer,Many2one,Selection,Binary,Many2many,Char
    """
    _name = 'college_management.college_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'college management module create'
    name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    contacts = fields.Char(string="Contact")
    age = fields.Integer(string="Age")
    # depart_id = fields.Many2one('res.partner',string="Department")
    state_id = fields.Selection([('pending', 'pending'),
                                 ('ongoing', 'ongoing'),
                                 ('completed', 'completed')],
                                string="state_id")
    # color = fields.Integer()
    photo_id = fields.Binary(string="Upload your photo")
    progress_bar = fields.Integer(string="progressbar")
    priority = fields.Selection([('0', 'Normal'),
                                 ('1', 'Good'),
                                 ('2', 'Very Good'),
                                 ('3', 'Excellent'),
                                 ('4', 'best')],
                                "Appreciation")
    email_id = fields.Char(string="Email")
    test_ids = fields.Many2many('hr.employee',
                                string='test')
    user_ids = fields.Many2many('res.country',
                                string='Users')
    user_signature = fields.Binary(string='Signature')
    # rating_avg = fields.Float("Rating Average")
    # image_id = fields.Binary(string='Image')
    url_id = fields.Char(string='URL')
    branch_id = fields.Selection([('option1', 'Information Technology'),
                                  ('option2', 'Computer'),
                                  ('option3', 'Civil'),
                                  ('option4', 'Mechanical')],
                                 tracking=True)
    my_field = fields.Selection([('option1', 'male'),
                                 ('option2', 'female')],
                                string="Gender")

    @api.onchange('name')
    def check(self):
        # if self.name:
            self.contacts = self.name

    @api.depends('value')
    def _value_pc(self):
        """
        function created for value2 field
        :return:
        """
        for record in self:
            record.value2 = float(record.value) / 100

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !")
    ]

    @api.model
    def create(self, vals):
        res = super(CollegeManagement, self).create(vals)
        print("vals------------------",vals,res)
        if vals.get('my_field') == 'option1':
            res['name'] = "Mr." + res['name']
        elif vals.get('my_field') == 'option2':
            res['name'] = "Mrs." + res['name']
        return res

    def write(self, vals):
        name = vals.get('name', self.name.split(".")[-1])
        if vals.get('my_field') == 'option1':
            vals['name'] = "Mr." + name
        elif vals.get('my_field') == 'option2':
            vals['name'] = "Mrs." + name

        res = super(CollegeManagement, self).write(vals)
        return res

    def create_record(self):
        """
        function to create a record
        :return: None
        """
        self.create({
            "name": "jake",
            "email_id": "jake@gmail.com",
            "url_id": "instagram.com",
            "my_field": "option1",
            "branch_id": "option3",
            "priority": "4"
        })

    def delete_record(self):
        """
        function to delete a record
        """

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'record deleted'
            }
        }

    def update_record(self):
        """
        function to update a record
        :return: updated record
        """
        self.write({
            "name": "kavish",
            "email_id": "kavish@gmail.com",
            "url_id": "odoo.com",
            "my_field": "option1",
            "branch_id": "option1",
            "priority": "1"
        })
