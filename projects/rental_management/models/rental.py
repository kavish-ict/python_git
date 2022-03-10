"""
new module
"""
from odoo import models, fields, api


class RentalManagement(models.Model):
    """
    class rental management with inherited model
    """
    _name = 'rental.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "create new object for rental"
    _rec_name = 'name'

    name = fields.Char(string="Name",
                       required=True, tracking=True)
    customer_id = fields.Many2one('res.partner',
                                  string="Customer", tracking=True)
    rental_type_id = fields.Many2one('rental.type',
                                     string="Rental Type", tracking=True)
    startdate = fields.Datetime(string="Start Date", tracking=True)
    enddate = fields.Datetime(string="End Date", tracking=True)
    rental_product_id = fields.Many2one('product.product',
                                        string="Rental Product")
    price = fields.Float(string="Price",
                         related="rental_product_id.list_price",
                         readonly=True, tracking=True)
    state = fields.Selection([('option1', 'Draft'),
                              ('option2', 'Waiting'),
                              ('option3', 'Approve'),
                              ('option4', 'Cancel')],
                             default="option1")

    @api.onchange('rental_type_id')
    def onchange_rental_type_id(self):
        for rec in self:
            print(rec.rental_type_id.id)
            return {'domain': {'rental_product_id': [('rental_type_id', '=', rec.rental_type_id.id)]}}

    # @api.onchange('name')
    # def test(self):
    #     """
    #     function to post a message in chatter
    #     """
    #     vals =
    #     self.message_post(body="record's name updated")
    #     self.write(vals)


class RentalType(models.Model):
    """
        class rental type with inherited model
        """

    _name = "rental.type"

    _description = "create new object for rental type"
    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    Description = fields.Text(string="Description")

    product_price = fields.Float(string="Product Price")

    _sql_constraints = [
        ('code_uniq', 'unique (code)', "Code must be unique"),
    ]
