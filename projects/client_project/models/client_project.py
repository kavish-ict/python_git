from odoo import models, fields, api


class ClientProject(models.Model):
    _name = 'client.project'
    _description = "Created this module."

    name = fields.Char(string="Name")
