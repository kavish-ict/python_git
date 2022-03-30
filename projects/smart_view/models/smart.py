"""
new module
"""
from odoo import models, fields


class SmartView(models.Model):
    """
    class smart view with inherited model
    """
    _name = 'smart.view'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "smart view module with sql _sql_constraints and api constraints"
    _rec_name = 'name_id'
    name_id = fields.Char(string="Name")
    new_field = fields.One2many('test.data', 'test_id',
                                string='new field')
    new_names = fields.Many2one('res.partner',
                                string="Names List")
    mobile_id = fields.Integer(string="Mobile",
                               tracking=True
                               )
    quantity_id = fields.Integer(string="Quantity", default="20")
    date_id = fields.Datetime(string='Date',
                              default=fields.Datetime.now)

    # _sql_constraints = [
    #         ('name_uniq', 'unique (name_id)', "Name is already in use"),
    #     ]

    _sql_constraints = [
        ('name_uniq', 'CHECK(quantity_id>0)', "Less Quantity "),
    ]

    def check(self):
        """
        function created to create a name record
        :return:
        """
        k = {'name_id': 'kavish'}
        return self.create(k)

    def create_record(self):
        """
        created record set
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

    # @api.constrains('name_id')
    # def test(self):
    #     for rec in self:
    #         if rec.name_id.isalpha() == False:
    #             raise ValidationError("invalid name")

    def test(self):
        """
        function to post a message in chatter
        """
        vals = {"name_id": "james"}
        self.message_post(body="record updated")
        self.write(vals)

    # @api.constrains('mobile_id')
    # def test_id(self):
    #     '''
    #     function to check that number must be 10 digits
    #     '''
    #     for rec in self:
    #         if len(rec.mobile_id) > 10:
    #             raise ValidationError("number is greater than 10 digits")
    #         elif len(rec.mobile_id) < 10:
    #             raise ValidationError("number is less than 10 digits")
    def create_one2many_record(self):
        # res = self.create({'name_id':"kavish",'new_field':[(0,0,{'new_name':"kavish shah"})]})
        # res = self.write({'name_id':"kavish",'new_field':[(0,0,{'new_name':"kavish shah"})]})
        # res = self.write({'new_field':[(1,137,{'new_name':"KAVISH SHAH"})]})
        vals = {'new_field': []}
        print("vals--------------------",vals)
        for rec in self.new_field:
            print("new field-----------------------------",self.new_field)
            vals['new_field'].append([1, rec.id, {'new_name': "KAVISH SHAH"}])
            print("rec--------------------",vals['new_field'])
        self.write(vals)


class TestView(models.Model):
    """
    class created for one to many fields
    """
    _name = 'test.data'
    test_id = fields.Many2one('smart.view',
                              string='Names')
    new_name = fields.Char(string='new name')
    product_id = fields.Many2one('res.country',
                                 string='product id')

    def func(self):
        """
        sample function
        :return:
        """
        return self

    def funt(self):
        """
        sample function
        :return:
        """
        return self
