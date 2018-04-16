# -*- coding: utf-8 -*-
from odoo import models, fields, api 
class WizardModel(models.TransientModel):
	_name = 'ideas.wizard'
	_description = 'Wizard_Ideas'
	rating = fields.Selection([
            ('0', 'bad'),
            ('1', 'okay'),
            ('2', 'good'),
            ('3', 'great'),
			('4', 'brilliant'),
            ],default='bad')
	comment = fields.Char('comment', required=True)
	
	