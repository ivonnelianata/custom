from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'


    #Attribute
    npwp = fields.Integer(string="NPWP", store=True)