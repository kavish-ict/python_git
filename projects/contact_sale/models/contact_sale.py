from odoo import models, fields, api


class ContactSale(models.Model):
    _name = 'contact.sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Created this module."
    _rec_name = 'new_name'

    new_name = fields.Char(string="Name", readonly=True)
    contact_id = fields.Many2one('res.partner', string='Contact')
    status = fields.Selection([('draft', 'Draft'),
                               ('in_progress', 'In Progress'),
                               ('done', 'Done'),
                               ('cancel', 'Cancel')], default="draft")
    no_follow_ups = fields.Integer(string="No. of Follow Ups", readonly=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale Order",
                                    domain="[('partner_id', '=',  contact_id)]")
    sales_person = fields.Many2one(string="Sales Person", related='sale_order_id.user_id', store=True)
    contact_sale_history_lines = fields.One2many('contact.sale.history', 'contact_sale',
                                                 string="Contact Sales History Lines")


    @api.model
    def create(self, vals):
        vals['new_name'] = self.env["ir.sequence"].next_by_code("contact.sale")
        return super(ContactSale, self).create(vals)

    def change_state_draft(self):
        self.status = "draft"
        # display_msg = "Contact Sale :" + self.contact_id.name + ", Sale Order : " + self.sale_order_id.name
        self.message_post(
            body='Contact Sale: %s <br/>Sale Order : %s ' % (self.contact_id.name, self.sale_order_id.name))
        self.no_follow_ups = self.no_follow_ups + 1
        print("---------------------------------------------")
        # new_lines = []
        # var = self.status
        # for res in self:
        #     new_lines.append((0, 0, {
        #         'contact_sale': res.new_name,
        #         'old_state': var,
        #         'new_state': res.status,
        #         'old_follow_ups': res.no_follow_ups - 1,
        #         'new_follow_ups': res.no_follow_ups
        #     }))
        # print("________________________________________new lines", new_lines)
        # self.write({'contact_sale_history_lines': [(0, 0, new_lines)]})

    def state_progress(self):
        self.status = "in_progress"
        self.message_post(
            body='Contact Sale: %s <br/>Sale Order : %s ' % (self.contact_id.name, self.sale_order_id.name))
        self.no_follow_ups = self.no_follow_ups + 1
        # new_lines = []
        # var = self.status
        # for res in self:
        #     new_lines.append((0, 0, {
        #         'contact_sale': res.new_name,
        #         'old_state': var,
        #         'new_state': res.status,
        #         'old_follow_ups': res.no_follow_ups - 1,
        #         'new_follow_ups': res.no_follow_ups
        #     }))
        # print("________________________________________new lines", new_lines)
        # self.write({'contact_sale_history_lines': [(0, 0, new_lines)]})

    def change_state_done(self):
        self.status = "done"
        self.message_post(
            body='Contact Sale: %s <br/>Sale Order : %s ' % (self.contact_id.name, self.sale_order_id.name))
        self.no_follow_ups = self.no_follow_ups + 1
        # new_lines = []
        # for res in self:
        #     new_lines.append((0, 0, {
        #         'contact_sale': res.new_name,
        #         'old_state': res.status,
        #         'new_state': res.status,
        #         'old_follow_ups': res.no_follow_ups - 1,
        #         'new_follow_ups': res.no_follow_ups
        #     }))
        # print("________________________________________new lines", new_lines)
        # self.update({'contact_sale_history_lines': new_lines})

    def change_state_cancel(self):
        self.status = "cancel"
        self.message_post(
            body='Contact Sale: %s <br/>Sale Order : %s ' % (self.contact_id.name, self.sale_order_id.name))
        self.no_follow_ups = self.no_follow_ups + 1
        # new_lines = []
        # for res in self:
        #     new_lines.append((0, 0, {
        #         'contact_sale': res.new_name,
        #         'old_state': res.status,
        #         'new_state': res.status,
        #         'old_follow_ups': res.no_follow_ups - 1,
        #         'new_follow_ups': res.no_follow_ups
        #     }))
        # print("________________________________________new lines", new_lines)
        # self.update({'contact_sale_history_lines': new_lines})

    def write(self, vals):
        # print("--------------------result------------------", result)
        # print("-------------new---state---------------", vals)
        # new_lines = []
        # for res in self:
        #     new_lines.append((0, 0, {
        #         'contact_sale': res.new_name,
        #         'old_state': temp,
        #         'new_state': res.status,
        #         'old_follow_ups': res.no_follow_ups - 1,
        #         'new_follow_ups': res.no_follow_ups
        #     }))
        # print("________________________________________new lines", new_lines)
        vals.update({'contact_sale_history_lines': [(0, 0, {'contact_sale': self.new_name,
                                                            'old_state': self.status,
                                                            'new_state': vals.get('status'),
                                                            'old_follow_ups': self.no_follow_ups,
                                                            'new_follow_ups': self.no_follow_ups + 1})]})
        return super(ContactSale, self).write(vals)



    # @api.onchange('status')
    # def on_change_state(self):
    #     print("---------------------------------------------")
    #     new_lines = []
    #     for res in self:
    #         new_lines.append((0, 0, {
    #             'contact_sale': res.new_name,
    #             'old_state': res.status,
    #             'new_state': res.status,
    #             'old_follow_ups': res.no_follow_ups,
    #         }))
    #     print("________________________________________new lines", new_lines)
    #     self.update({'contact_sale_history_lines': new_lines})


class ContactSaleHistory(models.Model):
    _name = 'contact.sale.history'
    _description = "Created this module."

    contact_sale = fields.Many2one('contact.sale', string="Contact Sale")
    old_follow_ups = fields.Integer(string='old follow ups')
    new_follow_ups = fields.Integer(string='new follow ups')
    old_state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'),
                                  ('done', 'Done'),
                                  ('cancel', 'Cancel')])
    new_state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'),
                                  ('done', 'Done'),
                                  ('cancel', 'Cancel')])
