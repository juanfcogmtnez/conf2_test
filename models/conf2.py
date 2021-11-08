# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)

class Conf2(models.Model):
	_name = "conf2"
	name = fields.Char(string="Proyecto")
	state = fields.Selection(
        	[('creado', 'Creado'),
         	('espacios', 'Obteniendo plan de espacios'),
         	('equipando', 'Equipando'),
			('definiendo','Definiendo marcas/modelos'),
			('consolidado','Consolidado'),
			('enviado','Enviado')],
        	'State', default="creado")
        	fecha_ini = fields.Date(string="Fecha Inicio")
        	fecha_fin = fields.Date(string="Fecha Fin")
        	child_ids =fields.One2many('tarea','parent_id', string = 'Espacios')


	def create_tarea(self):
		logger.info('in self:',self.id)
		record = self.env['tarea'].create({'parent_id':self.id})
