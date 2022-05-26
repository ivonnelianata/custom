from odoo import models, fields, api, _
#untuk translate

class nilai(models.Model): #inherit dari Model
    _name = 'khs.nilai' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg nilai'

    #membuat attribute field
    name = fields.Char('Number', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    mk = fields.Char('MK', size=64, required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    grade = fields.Char('Grade', size=64, required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    sks = fields.Char('SKS MK', size=64, required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})

    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    mahasiswa = fields.Many2one('khs.khs', string='Mahasiswa', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")

    #baru ditambahkan
    khs_id = fields.Many2one('khs.khs', string='Khs', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")


    def action_done(self):
        self.state = 'done'
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'

