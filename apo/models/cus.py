from odoo import models, fields, api, _
from odoo.exceptions import UserError
#untuk translate

class anggota(models.Model): #inherit dari Model
    _name = 'apo.cus' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk berlatih ttg customer'

    #membuat attribute field
    name = fields.Char('Nama Customer', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})  # index true krn field ini yg biasanya
    #name = fields.Many2one('res.partner', 'Confirm By', readonly=True)
    number = fields.Char('Number', size=64, required=True, index=True, readonly=True, default="new",
                         states={})
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
        ('number_uniq', 'UNIQUE (number)', 'You can not have two users with the same code !')
    ]
    def action_done(self):
        self.state = 'done'
        if self.number == 'new' or not self.number:
            seq = self.env['ir.sequence'].search([("code", "=", "apo.cus")])
            if not seq:
                raise UserError(_("apo.cus sequence not found, please create apo.cus sequence"))
            # self.name = seq.next_by_id(sequence_date=self.date)
            self.number = seq.next_by_id()  # kalo ga pake tahun langsung kosongan gini, kalo ada tahun pake yg atas
    def action_canceled(self):
        self.state = 'canceled'
    def action_settodraft(self):
        self.state = 'draft'