# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)

class Conf2(models.Model):
	_name = "conf2"
	name = fields.Char(string="Proyecto",required=True)
	state = fields.Selection(
        	[('creado', 'Creado'),
         	('curso', 'En curso'),
         	('revision', 'En revision'),
		('enviado','Enviado')],
        	'State', default="creado")
	fecha_ini = fields.Date(string="Fecha Inicio")
	fecha_fin = fields.Date(string="Fecha Fin")
	child_tareas_ids =fields.One2many('tarea','parent_id', string = 'Tareas configuración')
	child_documental_ids = fields.One2many('documental','parent_id',string = 'Tareas documentales')
	estudios = fields.Boolean(string="¿Incluye estudios?")
	estudios_ini = fields.Date(string="Fecha Inicio")
	estudios_fin = fields.Date(string="Fecha Fin (estimada)")
	estudios_resp = fields.Many2one('res.users','Responsable realización')
	estudios_resp_id = fields.Integer(related="estudios_resp.id", readonly=True)
	mapa = fields.Boolean(string="¿Incluye mapa?")
	mapa_ini = fields.Date(string="Fecha Inicio")
	mapa_fin = fields.Date(string="Fecha Fin (estimada)")
	mapa_resp = fields.Many2one('res.users','Responsable realizacion')
	mapa_resp_id = fields.Integer(related="mapa_resp.id", readonly=True)
	plan_funcional = fields.Boolean(string="¿Incluye plan funcional?")
	plan_funcional_ini = fields.Date(string="Fecha Inicio")
	plan_funcional_fin = fields.Date(string="Fecha Fin (estimada)")
	plan_funcional_resp = fields.Many2one('res.users','Responsable realizacion')
	plan_funcional_resp_id = fields.Integer(related="plan_funcional_resp.id", readonly=True)
	plan_espacios = fields.Boolean(string="¿Incluye plan de espacios?")
	plan_espacios_ini = fields.Date(string="Fecha Inicio")
	plan_espacios_fin = fields.Date(string="Fecha Fin (estimada)")
	plan_espacios_resp = fields.Many2one('res.users','Responsable realizacion')
	plan_espacios_resp_id = fields.Integer(related="plan_espacios_resp.id", readonly=True)
	plan_equipamiento = fields.Boolean(string="¿Incluye plan de equipamiento?")
	plan_equipamiento_ini = fields.Date(string="Fecha Inicio")
	plan_equipamiento_fin = fields.Date(string="Fecha Fin (estimada)")
	plan_equipamiento_resp = fields.Many2one('res.users','Responsable realizacion')
	plan_equipamiento_resp_id = fields.Integer(related='plan_equipamiento_resp.id',readonly=True)

	def create_tarea(self):
		logger.info('in self:',self.id)
		logger.info('estudios:',self.estudios)
		logger.info('mapa:',self.mapa)
		logger.info('funcional:',self.plan_funcional)
		logger.info('espacios:',self.plan_espacios)
		logger.info('equipamiento:',self.plan_equipamiento)
		logger.info('plan_equipamieto_resp:',self.plan_equipamiento_resp_id)
		nombre = self.name
		tareas = []
		documentales = []
		if self.estudios == True:
			documentales.append('estudio')
		if self.mapa == True:
			documentales.append('mapa')
		if self.plan_funcional == True:
			documentales.append('plan funcional')
		if self.plan_espacios == True and self.plan_equipamiento == False:
			tareas.append('plan de espacios')
		if self.plan_equipamiento == True and self.plan_espacios ==False:
			tareas.append('plan de espacios obl')
			tareas.append('plan de equipamiento')
		if self.plan_equipamiento == True and self.plan_espacios == True:
			tareas.append('plan de equipamiento')
			tareas.append('plan de espacios')
		for documental in documentales:
			if documental == 'estudio':
				record = self.env['documental'].create({'parent_id':self.id,'name':documental+' '+nombre,'fecha_ini':self.estudios_ini,'fecha_fin':self.estudios_fin,'responsable':self.estudios_resp_id})
			if documental  == 'mapa' :
				record = self.env['documental'].create({'parent_id':self.id,'name':documental+' '+nombre,'fecha_ini':self.mapa_ini,'fecha_fin':self.mapa_fin,'responsable':self.mapa_resp_id})
			if documental == 'plan funcional':
				record = self.env['documental'].create({'parent_id':self.id,'name':documental+' '+nombre,'fecha_ini':self.plan_funcional_ini,'fecha_fin':self.plan_funcional_fin,'responsable':self.plan_funcional_resp_id})


		for tarea in tareas:
			if tarea == 'plan de espacios':
				record = self.env['tarea'].create({'parent_id':self.id,'name':tarea+' '+nombre,'fecha_ini':self.plan_espacios_ini,'fecha_fin':self.plan_espacios_fin,'responsable':self.plan_espacios_resp_id})
			if tarea == 'plan de equipamiento':
				record = self.env['tarea'].create({'parent_id':self.id,'name':tarea+' '+nombre,'fecha_ini':self.plan_equipamiento_ini,'fecha_fin':self.plan_equipamiento_fin,'responsable':self.plan_equipamiento_resp_id})
			if tarea == 'plan de espacios obl':
				record = self.env['tarea'].create({'parent_id':self.id,'name':tarea+' '+nombre,'fecha_ini':self.plan_equipamiento_ini,'fecha_fin':self.plan_equipamiento_fin,'responsable':self.plan_equipamiento_resp_id})
