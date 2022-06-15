from odoo import models, fields, api

# _ utk translate
class detail(models.Model): #inherit dr Model
    _name = 'apo.detail' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data detail transaksi'

    #membuat attribute field
    detail_id = fields.Char('Detail Id', size=64, required=True, index=True, readonly=False) #index true krn field ini yg biasanya
    transaksi_id = fields.Many2one('apo.transaksi', string='Transaksi Id', index=True, readonly=False,
                                   ondelete="cascade")
    obat_id = fields.Many2one('apo.obat', string='Obat Id', index=True, readonly=False,
                              ondelete="cascade")
    harga =  fields.Integer("Harga", related='obat_id.hargaJual', store=True, readonly=True)
    hargaBeli = fields.Integer("Harga", related='obat_id.hargaBeli', store=True, readonly=True)
    # satuan = fields.Char("Satuan", related='obat_id.satuan', store=True, readonly=True)
    #tgl_wajibkembali = fields.Date('Tanggal Wajib Kembali', readonly=True)
    qty = fields.Integer("Qty", store=True, readonly=False)
    jumlah = fields.Integer("Jumlah", compute="_compute_jumlah", store=True, readonly=True)

    @api.depends('qty', 'harga')
    def _compute_jumlah(self):
        for rec in self:
            rec.jumlah = rec.harga * rec.qty


    def action_done(self):
        for rec in self:
            rec.state= 'done'
        #self.state = 'done'

    def action_canceled(self):
        for rec in self:
            rec.state= 'canceled'
        #self.state = 'canceled'

    def action_settodraft(self):
        for rec in self:
            rec.state= 'draft'
        #self.state = 'draft'