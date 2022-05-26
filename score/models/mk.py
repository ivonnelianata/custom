from odoo import models, fields, api
# _ utk translate
class mk(models.Model): #inherit dr Model
    _name = 'score.mk' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data MK'

    #membuat attribute field
    kode = fields.Char('Kode MK', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    name = fields.Char('Nama MK', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    sks = fields.Char('SKS', size=64, required=True, index=True, readonly=True,
                         states={'draft': [('readonly', False)]})

    #mk_ids = fields.One2many('nilai.detail', 'mk_id', string='MK')
    #sks_ids = fields.One2many('nilai.detail', 'sks_id', string='SKS')
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    #_sql_constraints = [('name_unik', 'unique(name)', _('Name must be unique!'))]
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two MK with the same name !')
    ]
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'