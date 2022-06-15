from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    npwp = fields.Float(string="NPWP", store=True, default="123")
