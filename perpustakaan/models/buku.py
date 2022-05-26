from odoo import models, fields, api
# _ utk translate
class buku(models.Model): #inherit dr Model
    _name = 'perpustakaan.buku' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data buku'

    #membuat attribute field
    name = fields.Char('Nama Buku', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    kode = fields.Char('Kode', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    tahun = fields.Char('Tahun', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    pengarang = fields.Char('Pengarang', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    penerbit = fields.Char('Penerbit', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    status = fields.Selection([('tersedia', 'Tersedia'),
                             ('tidak_tersedia', 'Tidak tersedia')
                             ], required=True,
                            readonly=True,
                            states={'draft': [('readonly', False)]})
    #kategori
    kategori_id = fields.Many2one('perpustakaan.kategori', string='Kategori', index=True, readonly=False,
                              ondelete="cascade")

    #harga
    harga = fields.Integer("Harga", default=5000, store=True, readonly=False)

    #stok
    #stok = fields.Integer("Stok", default=5, store=True, readonly=False)
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two users with the same name !'),
        ('kode_uniq', 'UNIQUE (kode)', 'You can not have two users with the same code !')
    ]

    def tes_bookrent(self):
        print("Ini hasil di book")
        t = self.env.context
        print(t.description)
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'