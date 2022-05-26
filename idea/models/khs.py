from odoo import models, fields, api, _
#untuk translate

class khs(models.Model): #inherit dari Model
    _name = 'khs.khs' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg khs'

    #membuat attribute field
    name = fields.Char('Mahasiswa', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    semester = fields.Char('Semester', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    tahun = fields.Char('Tahun', size=64, required=True, index=True, readonly=True,
                           states={'draft': [('readonly', False)]})
    ips = fields.Char('IPS', size=64, required=True, index=True, readonly=True,
                        states={'draft': [('readonly', False)]})
    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    #baru ditambah setelah nilai

    nilai_ids = fields.One2many('khs.nilai', 'khs_id', string='Penilai')

    def action_done(self):
        self.state = 'done'
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'

