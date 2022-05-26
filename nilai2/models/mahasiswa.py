from odoo import models, fields, api, _
#untuk translate

class mahasiswa(models.Model): #inherit dari Model
    _name = 'nilai.mahasiswa' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg mahasiswa'

    #membuat attribute field
    name = fields.Char('Nama Mahasiswa', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    nrp = fields.Char('NRP', size=64, required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    ipk = fields.Char('IPK', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})

    status = fields.Selection([('aktif', 'Aktif'),
                               ('cuti', 'Cuti'),
                               ('do', 'DO'),
                               ('lulus', 'Lulus')], required=True,
                              readonly=True,
                              states={'draft': [('readonly', False)]})
    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    _sql_constraints = [('name_unik', 'unique(name)', _('Name must be unique!'))]
    _sql_constraints = [('nrp_unik', 'unique(nrp)', _('NRP must be unique!'))]
    def action_done(self):
        self.state = 'done'
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'