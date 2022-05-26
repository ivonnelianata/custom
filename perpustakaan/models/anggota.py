from odoo import models, fields, api, _
#untuk translate

class anggota(models.Model): #inherit dari Model
    _name = 'perpustakaan.anggota' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg anggota'

    #membuat attribute field
    name = fields.Char('Nama Anggota', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    #name = fields.Many2one('res.partner', 'Confirm By', readonly=True)
    kode = fields.Char('Kode', size=64, required=True, index=True, readonly=True,
                         states={'draft': [('readonly', False)]})
    alamat = fields.Char('Alamat', size=64, required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    telp = fields.Char('Telp', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    jns_kelamin = fields.Selection(
        [('pria', 'Pria'),
         ('wanita', 'Wanita')], 'Jenis Kelamin', required=True, readonly=True,  states={'draft': [('readonly', False)]})
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