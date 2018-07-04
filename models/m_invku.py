# -*- coding:utf-8 -*-
from odoo import models, fields, api

import odoo.addons.decimal_precision as dp

class ProductChange(models.Model):
	_inherit = 'product.template'

	description = fields.Text(translate=False)
	description_purchase = fields.Text(translate=False)
	description_sale = fields.Text(translate=False)
	description_picking = fields.Text(translate=False)

	name = fields.Char(translate=False)
	_sql_constraints = [
		('name_uniq', 'unique(name)', '件号必须唯一!'),
	 ]

class PartnerChange(models.Model):
	_inherit = 'res.partner'

	_sql_constraints = [
		('name_uniq', 'unique(name)', '供应商/客户有重名情况发生!'),
	 ]




class ProductHidePrice(models.Model):
	_inherit = 'product.supplierinfo'
	price = fields.Float(
		'Price', default=0.0, digits=dp.get_precision('Product Price'),
		required=True, groups = 'purchase.group_purchase_manager,account.group_account_manager,purchase.group_purchase_user,base.group_system')
