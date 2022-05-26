from odoo import models, fields, api, _
# _ utk translate
class kelas(models.Model): #inherit dr Model
    _name = 'score.kelas' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data kelas yang dibuka pada suatu semester'

    #membuat attribute field
    name = fields.Char(compute="_compute_name", size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    state = fields.Selection(
        [('draft', 'Draft'),
         # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    tahun = fields.Char('Tahun', size=15,default="2021/2022", required=True, readonly=True,  states={'draft': [('readonly', False)]})
    semester = fields.Selection(
        [('Genap', 'Genap'),
         ('Gasal', 'Gasal'),
         ], 'Semester', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='Genap',  states={'draft': [('readonly', False)]})
    state = fields.Selection(
            [('draft', 'Draft'),
             # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
             ('done', 'Done'),
             ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh state

    mk_id = fields.Many2one('score.mk', string='Mata Kuliah', readonly=True, ondelete="cascade",
                                   states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done')]")
    line_ids = fields.One2many('score.kelas.lines', 'kelas_id', string='Nilai',readonly=True,  states={'draft': [('readonly', False)]})

    #_sql_constraints = [('name_unik', 'unique(name)', _('Name must be unique!'))]
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (mk_id.name, tahun, semester)', 'You can not have two users with the same name !')
    ]
    @api.depends('mk_id.name', 'semester', 'tahun')
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s - %s" % (s.mk_id.name, s.semester, s.tahun)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

    def action_wiz_nilai(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Wizard Nilai Kelas'),
            'res_model': 'wiz.score.kelas',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }


class kelas_lines(models.Model):
    _name = 'score.kelas.lines'
    _description = 'class untuk menyimpan data nilai suatu kelas'

    kelas_id = fields.Many2one('score.kelas', string='Kelas', ondelete='cascade')
    mhs_id = fields.Many2one('score.mahasiswa', string='Mahasiswa', ondelete='restrict')
    grade = fields.Selection([('A','A'),
                              ('B+', 'B+'),
                              ('B', 'B'),
                              ('C+', 'C+'),
                              ('C', 'C'),
                              ('D', 'D'),
                              ('E', 'E')])
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (kelas_id, mhs_id)', 'You can not have two users with the same name !')
    ]