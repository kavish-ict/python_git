from odoo import models, fields, api


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
    order_ids = fields.Many2many('sale.order', string="Sale Order",
                                 domain="[('user_id', '=',  responsible_id)]")
    operation_date = fields.Datetime(string="Operation Date")

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
        self.status = "done"
        self.order_ids.update({'date_order': self.operation_date})
        if self.operation_type == "confirm":
            self.order_ids.update({'state': "sale"})
        elif self.operation_type == "cancel":
            self.order_ids.update({'state': "cancel"})
        elif self.operation_type == "merge":
            self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
                'order_line': self.order_ids.order_line,
            })
            self.order_ids.update({'state': "cancel"})

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

    @api.onchange('responsible_id', 'operation_type', 'partner_id')
    def onchange_get_value_c(self):
        """
        function to set domain to select sale order
        """
        for rec in self:
            if rec.operation_type == "confirm":
                return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent']),
                                                 ('user_id', '=', self.responsible_id.id)]}}
            elif rec.operation_type == "cancel":
                return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent', 'sale']),
                                                 ('user_id', '=', self.responsible_id.id)]}}
            elif rec.operation_type == "merge":
                return {'domain': {'order_ids': [('state', 'in', ['draft', 'sent']),
                                                 ('user_id', '=', self.responsible_id.id),
                                                 ('partner_id', '=', self.partner_id.id)]}}
