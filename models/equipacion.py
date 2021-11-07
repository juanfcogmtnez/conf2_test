# -*- coding:utf-8 -*-

import logging

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Equipacion(models.Model):
	_name='equipacion'
	name = fields.Char(string='codigo_equipo')
	equipo = fields.Char(string='Nombre equipo')
	parent_id = fields.Many2one('espacios',string='Local',ondelete='restrict',index=True)
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
