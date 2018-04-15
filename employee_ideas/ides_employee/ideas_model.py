# -*- coding: utf-8 -*-
from odoo import models, fields, api
class EmployeeIdeas(models.Model):
	_name = 'employee.ideas'
	_inherit = ['mail.thread']
	_description = 'Employee Ideas'
	state = fields.Selection([
            ('new', 'New'),
            ('waiting', 'Waiting for Approval'),
            ('approved', 'Approved'),
            ('closed', 'Closed'),
            ],default='new')
	title = fields.Char('Title', required=True)
	employee = fields.Many2one('res.users', 'Employee')
	create_date = fields.Date('Create Date')
	company = fields.Many2one('res.company', 'Company')
	department = fields.Char('Department')
	deadline = fields.Date('Deadline', required=True)
	idea_type = fields.Many2one('idea.types', 'Idea Type')
	details = fields.Text('Details', required=True)
	vote = fields.Char('Votes')
