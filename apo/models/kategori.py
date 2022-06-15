from odoo import models, fields, api, _
from odoo.exceptions import UserError
# _ utk translate
class kategori(models.Model): #inherit dr Model
    _name = 'apo.kategori' #attribut dari class Model (lihat dokumen odoo)
    _description = 'class untuk menyimpan data kategori'

    #membuat attribute field
    name = fields.Char('Kategori', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    number = fields.Char('Number', size=64, required=True, index=True, readonly=True,default="new",states={})
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
            seq = self.env['ir.sequence'].search([("code", "=", "apo.kategori")])
            if not seq:
                raise UserError(_("apo.kategori sequence not found, please create apo.kategori sequence"))
            #self.name = seq.next_by_id(sequence_date=self.date)
            self.number = seq.next_by_id() #kalo ga pake tahun langsung kosongan gini, kalo ada tahun pake yg atas

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

    # @api.model_create_multi
    # def create(self, vals_list):
    #     if self.name == 'new' or not self.name:
    #         seq = self.env['ir.sequence'].search([("code", "=", "idea.voting")])
    #         if not seq:
    #             raise UserError(_("idea.voting sequence not found, please create idea.voting sequence"))
    #         for val in vals_list:
    #             val['name'] = seq.next_by_id()
    #
    #         return super(kategori, self).create(vals_list)

