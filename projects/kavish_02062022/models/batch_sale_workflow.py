import json
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class BatchSaleWorkflow(models.Model):
    """
    class for Batch Sale Workflow
    """
    _name = 'batch.sale.workflow'
    _description = "if user selects Responsible and Operation type " \
                   "then user can select sale order sales person which user" \
                   "selected in Responsible"
    _rec_name = 'batch_sequence'

    batch_sequence = fields.Char(readonly=True)
    responsible_id = fields.Many2one('res.users', string="Responsible")
    operation_type = fields.Selection([('confirm', 'Confirm'),
                                       ('cancel', 'Cancel'),
                                       ('merge', 'Merge')], default="confirm")
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                               ('cancel', 'Cancel')], default="draft")
    partner_id = fields.Many2one('res.partner', string="Customer")
    order_ids = fields.Many2many('sale.order', string="Sale Order")
    # order_ids_domain = fields.Char(compute="_compute_order_ids_domain", readonly=True, store=False)
    operation_date = fields.Datetime(string="Operation Date")
    batch_tags_ids = fields.Many2many('res.partner.category', string="Tags", related="partner_id.category_id", readonly=False)

    @api.model
    def create(self, vals):
        """
        function to set sequence
        """
        vals['batch_sequence'] = self.env["ir.sequence"].next_by_code("batch.sale.workflow")
        return super(BatchSaleWorkflow, self).create(vals)

    def proceed_operation(self):
        """
        function to set status done and to update date of sale order
        """
        view_id = self.env.ref('kavish_02062022.batch_order_wizard_form').id
        self.status = "done"
        self.order_ids.update({'date_order': self.operation_date})
        if self.operation_type == "confirm":
            if not self.operation_date:
                raise UserError(_('Please select Operation Date'))
            self.order_ids.action_confirm()
        elif self.operation_type == "cancel":
            if not self.operation_date:
                raise UserError(_('Please select Operation Date'))
            self.order_ids.action_cancel()
        elif self.operation_type == "merge":
            return {
                'name': "batch sale  wizard",
                'type': 'ir.actions.act_window',
                'res_model': 'batch.order.wizard',
                'view_mode': 'form',
                'view_id': view_id,
                'target': 'new'
            }
            # self.env['sale.order'].create({
            #     'partner_id': self.partner_id.id,
            #     'order_line': self.order_ids.order_line,
            # })
            # self.order_ids.update({'state': "cancel"})

    def status_cancel(self):
        """
        function to set status cancel
        """
        self.status = "cancel"

    def set_to_draft(self):
        """
        function to set status draft
        """
        self.status = "draft"

    # @api.depends('operation_type', 'responsible_id', 'partner_id')
    # def _compute_order_ids_domain(self):
    #     print("-----------------------------")
    #     for rec in self:
    #         if rec.operation_type == "confirm":
    #             rec.order_ids_domain = json.dumps(
    #                 [('state', 'in', ['draft', 'sent']), ('user_id', '=', self.responsible_id.id)])
    #             print("--------------------------------------", rec.order_ids_domain)
    #         elif rec.operation_type == "cancel":
    #             rec.order_ids_domain = json.dumps([('state', 'in', ['draft', 'sent', 'sale']),
    #                                                ('user_id', '=', self.responsible_id.id)])
    #         elif rec.operation_type == "merge":
    #             rec.order_ids_domain = json.dumps([('state', 'in', ['draft', 'sent']),
    #                                                ('user_id', '=', rec.responsible_id.id),
    #                                                ('partner_id', '=', rec.partner_id.id)])

    # @api.onchange('responsible_id', 'operation_type', 'partner_id')
    # def onchange_fields(self):
    #     """
    #     function to set domain to select sale order
    #     """
    #     res = {}
    #     res['domain'] = {'order_ids': []}
    #     for each in self:
    #         if each.operation_type == 'confirm':
    #             res['domain']['order_ids'].append(
    #                 ('state', 'in', ['draft', 'sent']))
    #         # if each.field_2:
    #         #     res['domain']['many2many_field'].append(('field_2', '=', each.field_2.id))
    #         # if each.field_3:
    #         #     res['domain']['many2many_field'].append(('field_3', '=', each.field_3.id))
    #         # if each.field_5:
    #         #     res['domain']['many2many_field'].append(('field_5', '=', each.field_5.id))
    #     return res
    # if rec.operation_type == "confirm":
    #     return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent']),
    #                                      ('user_id', '=', self.responsible_id.id)]}}
    # elif rec.operation_type == "cancel":
    #     return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent', 'sale']),
    #                                      ('user_id', '=', self.responsible_id.id)]}}
    # elif rec.operation_type == "merge":
    #     return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent']),
    #                                      ('user_id', '=', self.responsible_id.id),
    #                                      ('partner_id', '=', self.partner_id.id)]}}
