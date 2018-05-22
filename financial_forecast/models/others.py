# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Others(models.Model):
	_name = 'others.forecast'
	_description = 'others'
	
	nama = fields.Char('Nama', required=True)
	kategori = fields.Many2one('category.forecast', 'Category')
	tanggal_peminjaman = fields.Date('Tanggal Peminjaman')
	tenggat_waktu = fields.Date('Tenggat Waktu', required=True)
	total_biaya  = fields.Integer('Total Biaya')