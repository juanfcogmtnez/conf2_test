# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
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
	sub_ull_id = fields.Many2one('sub_ull',string="Plantilla SUB-Ull")
	sub_ull_2_id = fields.Many2one('sub_ull_2',string="Plantilla SUB-ULL-2")
	child_ids =fields.One2many('equipacion','parent_id', string = 'Equipos')
	definitivo = fields.Boolean(string="¿Es el plan de espacios definitivo?",default=True)
	completado = fields.Char(string="% Completado")
	state = fields.Selection(
		[('creado','Creado'),
			('curso','En curso'),
			('revision','En revisión'),
			('enviado','Enviado')],
			default='creado',string="Estado",group_expand='_get_stages'
		)
	def create_equipo(self):
		for record in self:
			logger.info('aqui van los records')
			logger.info(record)
		logger.info('in record:',record.id)
		logger.info('boton crear local')
		logger.info('este es mi padre')
		logger.info(record.parent_id.id)
		record = self.env['espacios'].create({'parent_id':record.id,'tarea_id':record.parent_id.id,'proyecto_id':record.proyecto_id.id})

	@api.model
	def is_allowed_transition(self, old_state , new_state):
		logger.info('allowed?')
		logger.info('este es el self')
		logger.info(self)
		logger.info('este es el old_state')
		logger.info(old_state)
		logger.info('este es el new_state')
		logger.info(new_state)
		allowed = [('creado','curso'),
			   ('curso','revision'),
			   ('revision','enviado'),
			   ('enviado','revision'),
			   ('revision','curso'),
			   ('curso','creado')]
		return (old_state, new_state) in allowed
	
	def change_state(self, new_state):
		logger.info('cambiando estado')
		logger.info('este es el self')
		logger.info(self)
		logger.info('este es el nuevo estado')
		logger.info(new_state)
		for project in self:
			logger.info('dentro del for')
			if project.is_allowed_transition(project.state,new_state):
				logger.info('dentro del if')
				project.state = new_state
			else:
				msg = _('Establecer desde %s a %s no está permitido') % (project.state, new_state)
				raise UserError(msg)
	def make_curso(self):
		self.change_state('curso')
	def make_revision(self):
		self.change_state('revision')
	def make_enviado(self):
		self.change_state('enviado')
		
	def ver_equipos(self):
		logger.info('hola soy el boton de equipos filtrados')
		logger.info('soy el self')
		logger.info(self)
		logger.info('somos los records')
		for record in self:
			logger.info(record)
		logger.info('hola soy')
		logger.info(record.name)
		view_id = self.env.ref('conf2.view_equipacion_tree').id
		return{
			'name':'Lista de equipos de proyecto',
			'view_type':'form',
			'view_mode':'tree',
			'views':[[view_id,'tree']],
			'res_model':'espacios',
			'type':'ir.actions.act_window',
			'domain':[('parent_id','=',record.name)],
			'target':'current',
		}

	def _get_stages(self, states, domain, order):
		
		return ['creado','curso','revision','enviado']
