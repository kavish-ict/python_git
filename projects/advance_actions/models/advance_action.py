from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for fields & orm methods."""
    _name = 'advance.action'
    _description = "Created this module."

    name = fields.Char(string="Name")
    designation = fields.Char(string="Designation")
    leave_date = fields.Date(string="Leave Date")
    phone = fields.Integer(string="Contact")
    email_id = fields.Char(string="Email")
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")

    def send_email(self):
        email_sent = self.env.ref('advance_actions.new_email_template').id
        self.env['mail.template'].browse(email_sent).send_mail(self.id, force_send=True)


class InheritResServerAction(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    def advance_action_change(self):
        """This is onchange api model."""
        # record_to_update = self.env['res.partner']
        # if record_to_update.exists():
        #     vals={}
        self.write({'name': 'Kavish Shah', 'phone': '+56 77989745634', 'email': 'kavish1234@gmail.com'})

    def advance_action_create(self):
        """This is onchange api model."""
        vals = {'name': 'Dhruv Shah', 'phone': '+34 67857868978', 'email': 'dhruvshah526@gmail.com'}
        self.env['res.partner'].create(vals)


class InheritSaleAction(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."

    def state_change(self):
        """This is onchange api model."""
        # for rec in self:
        #     if rec.state == 'draft':
        #         rec.state = 'sent'
        rec = self.search([]).write({"state": "sent"})
        print("---------------------------------", rec)
