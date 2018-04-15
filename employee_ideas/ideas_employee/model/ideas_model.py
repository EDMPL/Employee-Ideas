# -+- coding:utf-8 -+-
from odoo import models, fields, api
class EmployeeIdeas(models.Model):
	_name = 'employee.ideas'
	_description = 'Employee Ideas'
	title = fields.Char('Title', required=True)
	Employee = fields.Many2one('res.users','Employee')
	Create_date = fields.Date('Create Date')
	Company = fields.Many2one('res.company','Company')
	Department = fields.Many2one('emp.dept','Department')
	Deadline = fields.Date('Deadline')
	Ideas_type = fields.Char('Idea Type')
	vote = fields.Selection([
				('new', 'New'),
				('waiting', 'Waiting for Approval'),
				('approved', 'Approved'),
				('closed', 'Closed'),
				],default='new')
				
	@api.multi
	def post_progressbar(self):
		self.write({
		'vote': 'waiting'
		})