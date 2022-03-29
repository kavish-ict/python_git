from odoo import models, fields


class OrganizationExpense(models.Model):
    _name = "orphans.organization.expense"
    _description = "All orphan expenses are recorded here."

    expense_user = fields.Char(string="Name", help="Spender name..!", required=True)
    expense_type_id = fields.Many2one("expense.type",string="Expense type",required=True)
    currency_id = fields.Many2one("res.currency",
                                  string="Currency",
                                  default=20)
    expense_amount = fields.Monetary(string="Expense Amount", required=True)
    organization_id = fields.Many2one(comodel_name='orphans.organization', string="Orphans Home",required=True)
    notes = fields.Text(string="Notes")
