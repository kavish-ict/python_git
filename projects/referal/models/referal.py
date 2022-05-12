from odoo import models, fields, api


class ReferralApplication(models.Model):
    _name = 'hr.referral.application'
    _description = "Created this module."

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    referal_name_id = fields.Many2one('hr.employee', string="Referral Name")
    degree_id = fields.Many2one('hr.recruitment.degree', string="Degree")
    department_id = fields.Many2one('hr.job', string="Department")
    exp_salary = fields.Integer(string="Expected Salary")
    summary = fields.Text(string="Summary")
    exp_joining_date = fields.Date(string="Expected Joining Date")
    state = fields.Selection([('draft', 'Draft'), ('approve', 'Approved'),
                              ('cancel', 'Cancel')],
                             string="State", default='draft')

    def approve(self):
        for rec in self:
            rec.state = 'approve'

    def create_application(self):
        pass
