from odoo import models, fields, api
# _ utk translate
class detail(models.Model): #inherit dr Model
    _name = 'score.detail' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data score Mhs'

    #membuat attribute field
    grade = fields.Char('Grade', size=64, required=True, index=True, readonly=False)
    khs_id = fields.Many2one('score.khs', string='khs', readonly=False, ondelete="cascade")
    #mk_id = fields.Many2one('score.mk', string='mk', readonly=False, ondelete="cascade", states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")
    mk_id = fields.Many2one('score.mk', string='mk', readonly=False, ondelete="cascade")
                                   # states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")
    #paki ini yg kebaca pbo
    #sks_id = fields.Many2one('score.mk', string='sks', readonly=False, ondelete="cascade")
    sks_id = fields.Integer("SKS")

    #mk_ids = fields.Many2one('score.mk', string='mk', readonly=True, ondelete="cascade")
    #sks_id = fields.Many2one('mk_ids.sks', string='SKS', readonly=True, ondelete="cascade")
    #mk_id = fields.Many2one('mk_ids.kode', string='Kode MK', readonly=True, ondelete="cascade")