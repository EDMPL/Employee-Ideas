# -*- coding: utf-8 -*-
from odoo import models, fields, api 
class WizardModel(models.TransientModel):
	_name = 'ideas.wizard'
	_description = 'Wizard_Ideas'
	rating = fields.Selection([
            ('0', 'No Rate'),
            ('1', 'Bad'),
            ('2', 'Okay'),
            ('3', 'Good'),
            ('4', 'Great'),
			('5', 'Brilliant'),
            ],string='Rating')
	comment = fields.Char('Comment', required=True)
	