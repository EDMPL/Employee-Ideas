# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Payable(models.Model):
	_name = 'payable.forecast'
	_description = 'payable'
	description = fields.Char('Description', required=True)
	customer = fields.Char('Customer Name', required=True)
	order_date = fields.Date('Order Date')
	deadline = fields.Date('Deadline', required=True)
	revenue = fields.Integer('Revenue')