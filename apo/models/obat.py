from odoo import models, fields, api, _
from odoo.exceptions import UserError
# _ utk translate
class buku(models.Model): #inherit dr Model
    _name = 'apo.obat' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data obat'

    #membuat attribute field
    name = fields.Char('Nama Obat', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    number = fields.Char('Number', size=64, required=True, index=True, readonly=True, default="new",states={})
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    deskripsi = fields.Char('Deskripsi', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})

    satuan = fields.Selection([('tube', 'Tube'),
                               ('tablet', 'Tablet'),
                               ('botol', 'Botol'),
                               ], 'Satuan', required=True,
                              readonly=True,
                              states={'draft': [('readonly', False)]})
    #kategori
    kategori_id = fields.Many2one('apo.kategori', string='Kategori', index=True, readonly=False,
                           ondelete="cascade")
    #supplier
    supplier_id = fields.Many2one('apo.supplier2', string='Supplier2', index=True, readonly=False,
                                  ondelete="cascade")
    #harga
    hargaBeli = fields.Integer("Harga Beli", default=5000, store=True, readonly=False)
    hargaJual = fields.Integer("Harga Jual", default=5000, store=True, readonly=False)

    #stok
    stok = fields.Integer("Stok", default=5, store=True, readonly=False)
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two users with the same name !'),
        ('number_uniq', 'UNIQUE (number)', 'You can not have two users with the same code !')
    ]


    def action_done(self):
        self.state = 'done'
        if self.number == 'new' or not self.number:
            seq = self.env['ir.sequence'].search([("code", "=", "apo.obat")])
            if not seq:
                raise UserError(_("apo.obat sequence not found, please create apo.obat sequence"))
            #self.name = seq.next_by_id(sequence_date=self.date)
            self.number = seq.next_by_id() #kalo ga pake tahun langsung kosongan gini, kalo ada tahun pake yg atas

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'