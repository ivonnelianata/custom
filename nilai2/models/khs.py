from odoo import models, fields, api, _
#untuk translate

class khs(models.Model): #inherit dari Model
    _name = 'nilai.khs' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg khs'

    #membuat attribute field
    name = fields.Char(compute="_compute_name", store=True, recursive=True)  # index true krn field ini yg biasanya
    semester = fields.Selection([('genap', 'Genap'),
                                 ('gasal', 'Gasal'),
                                 ], 'Semester', required=True,
                                readonly=True,
                                states={'draft': [('readonly', False)]})
    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    #ips = fields.Float('IPS', compute="_compute_ips", store=True, default=0)
    tahun = fields.Char('Tahun', size=64, default="2021/2022", required=True, index=True, readonly=True,
                        states={'draft': [('readonly', False)]})

    #di khs ada mhs dari mahasiswa M:1
    mhs_id = fields.Many2one('nilai.mahasiswa', string='Mahasiswa', index=True, readonly=True, ondelete="cascade",
                             states={'draft': [('readonly', False)]})

    #baru ditambah setelah nilai_mh / detil khs ada
    detil_ids = fields.One2many('nilai.detil', 'khs_id2', string='Detil')
    #detail_ids = fields.One2many('nilai.detail', 'khs_id', string='Detail')
    @api.depends("mhs_id.name", "semester", "tahun")
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s - %s" % (s.mhs_id.name, s.semester, s.tahun)

    def action_done(self):
        self.state = 'done'
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'

