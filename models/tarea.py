# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)

class Tarea(models.Model):
	_name="tarea"
	name = fields.Char(string="Tarea")
	parent_id = fields.Many2one('conf2','Proyecto',index=True,ondelete='restrict')
	fecha_ini = fields.Date(string="Fecha incio")
	fecha_fin = fields.Date(string="Fecha fin")
	responsable = fields.Many2one('res.users',string='Responsable')
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
	child_ids =fields.One2many('espacios','parent_id', string = 'Equipos')
	completado = fields.Float(string="% Completado",compute="_completado",stored=True)
	state = fields.Selection(
								[
								('creado', 'Creado'),
								('espacios', 'Obteniendo plan de espacios'),
								('equipando', 'Equipando'),
								('definiendo','Definiendo marcas/modelos'),
								('consolidado','Consolidado'),
								('enviado','Enviado')
								],
								'State', default="creado"
								)

	def _completado(self):
		self.completado = 0.0

	'''
	@api.depends('child_ids')
	def _completado(self):
		logger.info('aquí la funcion completado')
		registros = 0
		grabados = 0
		for record in self:
			for linea in record.child_ids:
				logger.info(linea)
				registros = registros +1
				logger.info('caracteres ull:',len(linea.ull_id))
				if len(linea.ull_id) < 1:
					grabados = grabados
				else:
					grabados = grabados + 1
				logger.info('registros:',registros)
				logger.info('grabados:',grabados)
			if registros != 0:	
				self.completado = (grabados*100)/registros
			else:
				self.completado = 0
	'''
	def create_espacio(self):
		for record in self:
			logger.info('aqui van los records')
			logger.info(record)
		logger.info('in record:',record.id)
		logger.info('boton crear local')
		logger.info('este es mi padre')
		logger.info(record.parent_id.id)
		record = self.env['espacios'].create({'parent_id':record.id,'proyecto_id':record.parent_id.id})
