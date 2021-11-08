# -*- coding utf-8 -*-

import logging

from odoo import fields, models, api

logger = logging.getLogger(__name__)


class Espacios(models.Model):
	_name='espacios'
	name = fields.Char(string='codigo_local')
	padre = fields.Char(string="Padre")
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
	parent_id = fields.Many2one('conf2','Proyecto',index=True,ondelete='restrict')
	bloque = fields.Char(string="Bloque")
	planta = fields.Char(string="Planta")
	local = fields.Char(string="Local")
	superficie = fields.Char(string="m2")	
	ull_id = fields.Many2one('ull',string="Plantilla Ull")
	child_ids =fields.One2many('equipacion','parent_id', string = 'Equipos')
