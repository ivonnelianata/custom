from odoo import models, fields, api, _

# _ utk translate
class wiztransaksi(models.TransientModel): #inherit dr Model
    _name = 'wiz.apo.transaksi' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan wiz data transaksi'

    transaksi_id = fields.Many2one('apo.transaksi', string='Transaksi Id')
    #detail_ids = fields.Many2one('apo.detail', string='Transaksi Id')
    # di transaksi ada 1:M
    customer_id = fields.Many2one(related='transaksi_id.customer_id', string='Customer')

    #baru ditambah setelah detail
    detail_ids = fields.One2many('wiz.apo.transaksi.lines', 'wiz_header_id', string='Detail')

    #related field
    anggota_alamat = fields.Char("Alamat", related='transaksi_id.customer_id.alamat')
    tanggal = fields.Date(related="transaksi_id.tanggal", default=fields.Date.context_today)
    obat_id = fields.Many2one('apo.detail', string='Obat Id')
    harga = fields.Integer(related="obat_id.harga", string='Harga Id')
    hargaBeli = fields.Integer(related="obat_id.hargaBeli", string='Harga Beli')
    # detail_id=fields.One2many('wiz.apo.transaksi', 'wiz_header_id', string='DetailId')
    def action_done(self):
        #self.state = 'done'
        for rec in self.detail_ids:
            rec.ddetail_id.obat_id = rec.wiz_obat_id
            rec.ddetail_id.harga = rec.wiz_harga
            rec.ddetail_id.hargaBeli = rec.wiz_hargaBeli
    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

    @api.model
    def default_get(self,fields_list):  # ini adalah common method, semacam constructor, akan dijalankan saat create object. Ini akan meng-overwrite default_get dari parent
        res = super(wiztransaksi, self).default_get(fields_list)
        # res  merupakan dictionary beserta value yang akan diisi, yang sudah diproses di super class (untuk create record baru)
        res['transaksi_id'] = self.env.context['active_id']
        return res

    @api.onchange('transaksi_id')
    def onchange_transaksi_id(self):
        if not self.transaksi_id:
            return
        # vals = []
        detail_ids = self.env['wiz.apo.transaksi.lines']
        for rec in self.transaksi_id.detail_ids:
            detail_ids += self.env['wiz.apo.transaksi.lines'].new({
                'wiz_header_id': self.id,
                'wiz_obat_id': rec.obat_id,
                'wiz_harga' : rec.harga,
                'wiz_hargaBeli': rec.hargaBeli,
                'ddetail_id' : rec.id
                #'ref_transaksi_lines_id': rec.id
            })
            # cara membuat record baru di m2m atau o2m
        self.detail_ids = detail_ids

class transaksi_lines_wiz(models.TransientModel):
    _name = 'wiz.apo.transaksi.lines'
    _description = 'class untuk menyimpan data transaksi'

    wiz_header_id = fields.Many2one('wiz.apo.transaksi', string='ID Transaksi')
    # customer_id = fields.Many2one('apo.cus', string='Mahasiswa', ondelete="restrict")
    # ref_transaksi_lines_id = fields.Many2one('apo.transaksi.lines')
    wiz_obat_id = fields.Many2one('apo.obat', string='Obat Id')
    wiz_harga = fields.Integer(string='Harga Id')
    wiz_hargaBeli = fields.Integer(string='Harga Beli')
    ddetail_id = fields.Many2one('apo.detail')
    # obat_id = fields.Many2one('apo.obat', string='Obat Id')
    # dtransaksi_id = fields.Many2one('apo.transaksi')


