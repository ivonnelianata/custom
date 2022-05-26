from odoo import models, fields, api
# _ utk translate
class mahasiswa(models.Model): #inherit dr Model
    _name = 'score.mahasiswa' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data mahasiswa'

    #membuat attribute field
    name = fields.Char('Nama Mahasiswa', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    nrp = fields.Char('NRP', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    ipk = fields.Char('IPK', size=64, required=True, index=True, readonly=True,
                         states={'draft': [('readonly', False)]})
    status = fields.Selection([('aktif', 'Aktif'),
                             ('cuti', 'Cuti'),
                             ('do', 'DO'),
                             ('lulus', 'Lulus')], required=True,
                            readonly=True,
                            states={'draft': [('readonly', False)]})

    #_sql_constraints = [('name_unik', 'unique(name)', _('Name must be unique!'))]
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two users with the same name !')
    ]
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'