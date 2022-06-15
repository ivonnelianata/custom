from odoo import models, fields, api, _
from odoo.exceptions import UserError
# _ utk translate
class transaksi(models.Model): #inherit dr Model
    _name = 'apo.transaksi' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data transaksi'

    #membuat attribute field
    #name = fields.Char('kode', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    name = fields.Char(compute="_compute_name", store=True, recursive=True)  # index true krn field ini yg biasanya
    number = fields.Char('number', size=64, required=True, index=True, readonly=True, default="new", states={})
    total = fields.Integer("Total", compute="_compute_total", store=True, default=0)
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # di transaksi ada 1:M
    customer_id = fields.Many2one('apo.cus', string='Customer', index=True, readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]})

    #baru ditambah setelah detail
    detail_ids = fields.One2many('apo.detail', 'transaksi_id', string='Detail')

    #related field
    anggota_alamat = fields.Char("Alamat", related='customer_id.alamat')

    #biaya pinjam
    #total_pinjam = fields.Integer("Total Pinjam", compute="_compute_total_pinjam", store=True, default=0)

    #tanggal
    tanggal = fields.Date('Tanggal', default=fields.Date.context_today, readonly=True, help='Please fill the date',
                       states={'draft': [('readonly', False)]})

    #nama untuk transaksi
    @api.depends("customer_id.name", "number", "tanggal")
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s - %s" % (s.number, s.tanggal, s.customer_id.name)

    # def utk total total
    @api.depends("detail_ids", "state")
    def _compute_total(self):
        summ = 0
        for s in self:
            for rec in s.detail_ids:
                summ += rec.jumlah
            s.total = summ
            summ = 0

    def action_done(self):
        for rec in self:
            rec.state= 'done'
        if self.number == 'new' or not self.number:
            seq = self.env['ir.sequence'].search([("code", "=", "apo.transaksi")])
            if not seq:
                raise UserError(_("apo.transaksi sequence not found, please create apo.transaksi sequence"))
            #self.name = seq.next_by_id(sequence_date=self.date)
            self.number = seq.next_by_id() #kalo ga pake tahun langsung kosongan gini, kalo ada tahun pake yg atas

        #self.state = 'done'

    def action_wiz_transaksi(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Wizard Apo Transaksi'),
            'res_model': 'wiz.apo.transaksi',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }


    def action_canceled(self):
        for rec in self:
            rec.state= 'canceled'
        #self.state = 'canceled'

    def action_settodraft(self):
        for rec in self:
            rec.state= 'draft'
        #self.state = 'draft'


