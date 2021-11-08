# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)

class Documental(models.Model):
	_name="documental"
	name = fields.Char(string="Entregable")
	parent_id = fields.Many2one('conf2','Proyecto',index=True,ondelete='restrict')
	fecha_ini = fields.Date(string="Fecha incio")
	fecha_fin = fields.Date(string="Fecha fin")
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
	state = fields.Selection(
				[
				('creado', 'Creado'),
				('curso', 'En curso'),
				('revision', 'En revisión'),
				('entregado','Entregado'),
				],
				'State', default="creado"
				)
