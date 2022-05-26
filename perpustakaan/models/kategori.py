from odoo import models, fields, api
# _ utk translate
class kategori(models.Model): #inherit dr Model
    _name = 'perpustakaan.kategori' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data kategori'

    #membuat attribute field
    name = fields.Char('Kategori', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    kode = fields.Char('Kode', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    state = fields.Selection(
            [('draft', 'Draft'),
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,
            default='draft')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two users with the same name !'),
        ('kode_uniq', 'UNIQUE (kode)', 'You can not have two users with the same code !')
    ]
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'