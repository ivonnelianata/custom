from odoo import models, fields, api
# _ utk translate
class khs(models.Model): #inherit dr Model
    _name = 'score.khs' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data KHS'

    #membuat attribute field
    semester = fields.Char('Semester', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    tahun = fields.Char('Tahun', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]}) #index true krn field ini yg biasanya
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    ips = fields.Char('IPS', size=64, required=True, index=True, readonly=True,
                         states={'draft': [('readonly', False)]})

    mahasiswa_id = fields.Many2one('score.mahasiswa', string='Mahasiswa', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")

    detail_ids = fields.One2many('score.detail', 'khs_id', string='Detail')

    name = fields.Char(compute="_compute_name", store=True, recursive=True)  # index true krn field ini yg biasanya

    @api.depends("mahasiswa_id.name", "semester", "tahun")
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s - %s" % (s.mahasiswa_id.name, s.semester, s.tahun)
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'