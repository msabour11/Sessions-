from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"
    is_instructor = fields.Boolean(string="Instructor")
    session_ids = fields.Many2many('accademy.session',  string="Sessions")
