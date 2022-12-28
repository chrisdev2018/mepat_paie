# -*- coding: utf-8 -*-
from odoo import models, fields

class CentreRH(models.Model):
	_name = "mepat_paie.centre_rh"
	
	name = fields.Char(
		string="Nom",
		required=True
	)
	
	code = fields.Char(
		string="Code",
		required=True
	)
