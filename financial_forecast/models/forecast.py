# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Forecast(models.Model):
    _name = 'report.forecast'
    _description = 'report'

    tanggal = fields.Date('Tanggal')
    saldo_awal = fields.Integer('Saldo')
    payable_id = fields.Many2one('payable.forecast', string='Payable')
    receivable_id = fields.Many2one('receivable.forecast', string='Receivable')
    others_id = fields.Many2one('others.forecast', string='Others')
    total_biaya = fields.Integer('Total Biaya')
