from odoo import models, fields, api, _
#untuk translate

class detil(models.Model): #inherit dari Model
    _name = 'nilai.detil' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg nilai'

    #membuat attribute field
    mk_id = fields.Many2one('nilai.mk', string='MK_ID', index=True, readonly=True, ondelete="cascade",
                            states={'draft': [('readonly', False)]})
    khs_id = fields.Many2one('nilai.khs', string='KHS_ID', index=True, readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]})
    grade = fields.Char('Grade', size=64, required=True, index=True, readonly=True,
                        states={'draft': [('readonly', False)]})
    sks_id = fields.Many2one('mk_id.credit', string='SKS_ID', index=True, readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]})






