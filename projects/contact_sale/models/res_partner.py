from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Created this module."

    total_contact_sale = fields.Integer(compute='total_numbers')

    def total_numbers(self):
        for rec in self:
            domain = [('contact_id', '=', rec.id)]
            res = self.env['contact.sale'].search(domain)
            print("-------------------", res)
            rec.total_contact_sale = len(res)
            if len(res) > 1:
                view = 'tree,form'
            else:
                view = 'form'
        return {
            'name': 'contact sale',
            'view_mode': view,
            'res_model': 'contact.sale',
            'res_id': res.id if len(res) == 1 else False,
            'type': 'ir.actions.act_window',
            'domain': domain,
        }

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
