# -*- coding: utf-8 -*-
from odoo import models, fields, api
class CashCategory(models.Model):
	_name = 'category.forecast'
	_description = 'Cash Flow Category'
	name	= fields.Char(string='Category Name', required=True)
    