# -*- coding utf-8 -*-

import logging

from odoo import fields, models, api

logger = logging.getLogger(__name__)


class Espacios(models.Model):
	_name='espacios'
	name = fields.Char(string='codigo_local')
	_parent_store = True
	_parent_name = "parent_id"
	proyecto_id = fields.Many2one('conf2','Proyecto',index=True,ondelete='restrict')
	parent_path = fields.Char(index=True)
	parent_id = fields.Many2one('tarea','Tarea',index=True,ondelete='restrict')
	bloque = fields.Char(string="Bloque")
	planta = fields.Char(string="Planta")
	local = fields.Char(string="Local")
	sub_local = fields.Char(string="sub_local")
	superficie = fields.Char(string="m2")	
	ull_id = fields.Many2one('ull',string="Plantilla Ull")
	child_ids =fields.One2many('equipacion','parent_id', string = 'Equipos')
