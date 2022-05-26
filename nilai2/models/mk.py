from odoo import models, fields, api, _
#untuk translate

class mk(models.Model): #inherit dari Model
    _name = 'nilai.mk' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg mk'

    #membuat attribute field

    name = fields.Char('Nama MK', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    code = fields.Char('Kode MK', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    credit = fields.Integer('SKS', required=True, readonly=True,
                            states={'draft': [('readonly', False)]})
    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})

    _sql_constraints = [('name_unik', 'unique(name)', _('Name must be unique!'))]

    def action_done(self):
        self.state = 'done'
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'

