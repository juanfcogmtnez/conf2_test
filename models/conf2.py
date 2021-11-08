# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)

class Conf2(models.Model):
	_name = "conf2"
	name = fields.Char(string="Proyecto",required=True)
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
	estudios = fields.Boolean(string="¿Incluye estudios?")
	mapa = fields.Boolean(string="¿Incluye mapa?")
	plan_funcional = fields.Boolean(string="¿Incluye plan funcional?")
	plan_espacios = fields.Boolean(string="¿Incluye plan de espacios?")
	plan_equipamiento = fields.Boolean(string="¿Incluye plan de equipamiento?")

	def create_tarea(self):
		logger.info('in self:',self.id)
		logger.info('estudios:',self.estudios)
		logger.info('mapa:',self.mapa)
		logger.info('funcional:',self.plan_funcional)
		logger.info('espacios:',self.plan_espacios)
		logger.info('equipamiento:',self.plan_equipamiento)
		nombre = self.name
		tareas = []
		documentales = []
		if self.estudios == True:
			documentales.append('estudio')
		if self.mapa == True:
			documentales.append('mapa')
		if self.plan_funcional == True:
			documentales.append('plan funcional')
		if self.plan_espacios == True:
			tareas.append('plan de espacios')
		if self.plan_equipamiento == True and self.plan_espacios ==False:
			tareas.append('plan de espacios')
			tareas.append('plan de equipamiento')
		if self.plan_equipamiento == True and self.plan_espacios == True:
			tareas.append('plan de equipamiento')
		for tarea in tareas:
			record = self.env['tarea'].create({'parent_id':self.id,'name':tarea+' '+nombre})
		for documental in documentales:
			record = self.env['documental'].create({'parent_id':self.id,'name':documental+' '+nombre})
