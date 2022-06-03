"""This"""

from odoo import models, fields


class Exam(models.Model):
    """
    created class for exam_2 module
    """

    _name = 'exam'
    _description = "Created this module."

    name = fields.Char(string="name")
    age = fields.Integer(string="age")

