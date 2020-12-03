# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sales(models.Model):
    _inherit = 'sale.order'

    ref_number = fields.Char('Reference #')

    amount_undiscounted = fields.Monetary('Amount Before Discount', compute='_compute_amount_undiscounted', digits=0)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100