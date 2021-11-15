# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
logger = logging.getLogger(__name__)

class Documental(models.Model):
	_name="documental"
	name = fields.Char(string="Tarea")
	parent_id = fields.Many2one('conf2','Proyecto',index=True,ondelete='restrict')
	fecha_ini = fields.Date(string="Fecha incio")
	fecha_fin = fields.Date(string="Fecha fin")
	responsable = fields.Many2one('res.users',string='Responsable')
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
	completado = fields.Float(string="% Completado")
	state = fields.Selection(
				[('creado','Creado'),
				 ('curso','En curso'),
				 ('revision','En revisión'),
				 ('enviado','Enviado')],
				default='creado',string="Estado",group_expand='_get_stages'
				)

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

	def _get_stages(self, states, domain, order):
		
		return ['creado','curso','revision','enviado']
