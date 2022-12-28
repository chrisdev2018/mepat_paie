# -*- coding: utf-8 -*-
from odoo import fields, models, _


class PrimeInd(models.Model):

    _name = 'mepat_paie.prime_ind'
    _rec_name = 'code'

    regle_salariale = fields.Many2one(
        string='Regle salariale',
        required=False,
        readonly=False,
        help=u"Regle salariale lié",
        comodel_name='hr.salary.rule',
        ondelete="set null")

    code = fields.Char(
        string='Code',
        readonly=True,
        related="regle_salariale.code")

    contrat_id = fields.Many2one(
        string='Contrat',
        readonly=False,
        comodel_name='hr.contract')

    montant = fields.Float(
        string='Montant',
        required=True,
        default=0.0,
        digits=(16, 2))
