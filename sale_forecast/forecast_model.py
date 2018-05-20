# -*- coding: utf-8 -*-
from odoo import models, fields, api
class SaleForecast(models.Model):
    _name = 'receivable.forecast'
    _description = 'receivable'
    description = fields.Char('Description', required=True)
	customer = fields.Char('Customer Name', required=True)
	order_date = fields.Date('Order Date')
	deadline = fields.Date('Deadline', required=True)
	revenue = fields.Integer('Revenue')
	

  

   