from odoo import models, fields, api

# _ utk translate
class detail(models.Model): #inherit dr Model
    _name = 'perpustakaan.detail' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data detail transaksi'

    #membuat attribute field
    detail_id = fields.Char('Detail Id', size=64, required=True, index=True, readonly=False) #index true krn field ini yg biasanya
    tgl_pinjam = fields.Date('Tanggal Pinjam', default=fields.Date.context_today, readonly=False,
                             help='Please fill the date')
    transaksi_id = fields.Many2one('perpustakaan.transaksi', string='Transaksi Id', index=True, readonly=False,
                                   ondelete="cascade")
    tgl_kembali = fields.Date('Tanggal Kembali', readonly=False, help='Please fill the date')
    buku_id = fields.Many2one('perpustakaan.buku', string='Buku Id', index=True, readonly=False,
                              ondelete="cascade", domain="[('status', '=', 'tersedia'),('state', '=', 'done')]")
    tgl_wajibkembali = fields.Date('Tanggal Wajib Kembali', compute="_compute_wajib", readonly=False,
                                   help='Please fill the date')
    harga =  fields.Integer("Harga", related='buku_id.harga', store=True, readonly=True)

    #tgl_wajibkembali = fields.Date('Tanggal Wajib Kembali', readonly=True)
    durasi = fields.Integer("Durasi", compute="_compute_day", store=True, readonly=True)
    denda = fields.Integer("Denda", compute="_compute_denda", store=True, readonly=True)

    @api.depends('tgl_pinjam', 'tgl_kembali')
    def _compute_day(self):
        if self.tgl_pinjam and self.tgl_kembali:
            tgl_pinjam = fields.Datetime.from_string(self.tgl_pinjam)
            tgl_kembali = fields.Datetime.from_string(self.tgl_kembali)
            self.durasi = abs((tgl_kembali - tgl_pinjam).days)

    @api.depends('tgl_kembali')
    def _compute_denda(self):
        for rec in self:
            tgl_kembali = fields.Datetime.from_string(rec.tgl_kembali)
            tgl_wajibkembali = fields.Datetime.from_string(rec.tgl_wajibkembali)
            if rec.tgl_kembali:
                if rec.durasi > 7:
                    rec.denda = abs((tgl_kembali - tgl_wajibkembali).days) * 1000
                else:
                    rec.denda = 0


    @api.onchange('tgl_pinjam')
    def _compute_wajib(self):
        for rec in self:
            if rec.tgl_pinjam:
                tgl_pinjam = fields.Datetime.from_string(rec.tgl_pinjam)
                tgl_kembali = fields.Datetime.from_string(rec.tgl_kembali)
                rec.tgl_wajibkembali = fields.Datetime.add(fields.Datetime.now(),days=7)

    #@api.onchange('tgl_pinjam', 'buku_id.status')
    #def pinjaman_confirm (self):
     #   for rec in self:
      #      rec.buku_id.status = 'terpinjam'
       #     return rec.write({'status': 'terpinjam'})


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