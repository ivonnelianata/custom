from odoo import models, fields, api, _
#untuk translate

class detil(models.Model): #inherit dari Model
    _name = 'nilai.detil' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg nilai'

    # membuat attribute field
    mk_id2 = fields.Many2one('nilai.mk', string='MK_ID', readonly=True, ondelete="cascade")
    khs_id2 = fields.Many2one('nilai.khs', string='KHS_ID', readonly=True, ondelete="cascade")
    grade2 = fields.Char('Grade', size=64, required=True, index=True, readonly=False)
    sks_id2 = fields.Many2one('mk_id.credit', string='SKS_ID', readonly=True, ondelete="cascade")
    khs_id = fields.Many2one('nilai.khs', string='KHs', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")
    mk_id = fields.Many2one('nilai.mk', string='Mk', readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")
    grade = fields.Char('Grade', size=64, required=True, index=True, readonly=False)









