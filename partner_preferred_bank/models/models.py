# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerPreferredBank(models.Model):
    _inherit = 'res.partner'

    @api.depends_context('uid','company')
    def _calc_current_company_partner(self):
        self.ba_current_company_partner_id=self.env.company.partner_id
        
    ba_current_company_partner_id = fields.Many2one(string="Current company partner", comodel_name='res.partner', compute='_calc_current_company_partner')
    property_default_incoming_bank_account_id=fields.Many2one(string="Predefined BA for receiving payments", comodel_name='res.partner.bank', company_dependent=True, domain="[('partner_id','=',ba_current_company_partner_id)]", help="Preferred bank account to be used for receiving payments from customers")
    property_default_outgoing_bank_account_id=fields.Many2one(string="Predefined BA for making payments", comodel_name='res.partner.bank', company_dependent=True, domain="[('partner_id','=',ba_current_company_partner_id)]", help="Preferred bank account to be used for making payments to suppliers" )
    property_default_br_bank_account_id=fields.Many2one(string="Predefined customer BA for BR payments", comodel_name='res.partner.bank', company_dependent=True, domain="[('partner_id','=',id)]", help="Preferred bank account of the customer to be used for BR payments" )
