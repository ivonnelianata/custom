from odoo import models, fields, api
# _ utk translate
class transaksi(models.Model): #inherit dr Model
    _name = 'perpustakaan.transaksi' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data transaksi'

    #membuat attribute field
    #name = fields.Char('kode', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    name = fields.Char(compute="_compute_name", store=True, recursive=True)  # index true krn field ini yg biasanya
    kode = fields.Char('kode', size=64, required=True, index=True, readonly=True, states={'draft': [('readonly', False)]})
    total = fields.Integer("Total Denda", compute="_compute_total", store=True, default=0)
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # di transaksi ada 1:M
    anggota_id = fields.Many2one('perpustakaan.anggota', string='Anggota', index=True, readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]})

    #baru ditambah setelah detail
    detail_ids = fields.One2many('perpustakaan.detail', 'transaksi_id', string='Detail')

    #related field
    anggota_alamat = fields.Char("Alamat", related='anggota_id.alamat')

    #biaya pinjam
    total_pinjam = fields.Integer("Total Pinjam", compute="_compute_total_pinjam", store=True, default=0)

    #tanggal
    tanggal = fields.Date('Tanggal', default=fields.Date.context_today, readonly=True, help='Please fill the date',
                       states={'draft': [('readonly', False)]})

    #nama untuk transaksi
    @api.depends("anggota_id.name", "kode", "tanggal")
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s - %s" % (s.kode, s.tanggal, s.anggota_id.name)

    #def utk total denda
    @api.depends("detail_ids", "state")
    def _compute_total(self):
        summ = 0
        for s in self:
            for rec in s.detail_ids:
                 summ += rec.denda
            s.total = summ
            summ = 0

    # def utk total pinjam
    @api.depends("detail_ids", "state")
    def _compute_total_pinjam(self):
        sum = 0
        for s in self:
            for rec in s.detail_ids:
                sum += rec.harga
            s.total_pinjam = sum
            sum = 0


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


