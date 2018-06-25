# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Receivable(models.Model):
	_name = 'receivable.forecast'
	_description = 'receivable'
	
	Name = fields.Char('Name', required=True)
	Category = fields.Many2one('category.forecast', string='Category')
	Internal_Note = fields.Char('Internal Note', required=True)
	tanggal_transaksi = fields.Date('Transaction Date')
	tenggat_waktu = fields.Date('Deadline', required=True)
	total_biaya  = fields.Integer('Total Amount')