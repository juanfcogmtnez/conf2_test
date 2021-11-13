# -*- coding:utf-8 -*-

import logging

from odoo import fields, models, api

logger = logging.getLogger(__name__)

class Equipacion(models.Model):
	_name='equipacion'
	_inherit='equipamiento'
	name = fields.Char(string='codigo_equipo')
	proyecto_id = fields.Many2one('conf2',string='Proyecto',ondelete='restrict')
	tarea_id = fields.Many2one('tarea',string="Tarea",ondelete='restrict')
	parent_id = fields.Many2one('espacios',string='Local',ondelete='restrict',index=True)
	_parent_store = True
	_parent_name = "parent_id"
	parent_path = fields.Char(index=True)
	equipamiento_name = fields.Many2one('product.template', string="Nombre equipo Simalga")
	equipo_cliente = fields.Char(string="Nombre equipamiento cliente")
	cantidad = fields.Float(string="cantidad")
	unidad = fields.Char(string="Unidad de medida")
	name_es = fields.Char(string='Equipamiento')
	name_fr = fields.Char(string='Équipement')
	name_en = fields.Char(string='Equipment')
	ull_ids = fields.Char(string="ull")
	sub_ull_ids = fields.Char(string="sub ull")
	sub_ull_2_ids = fields.Char(string="sub ull 2")
	item_code = fields.Char(string="item-code")
	descripcion_es = fields.Text(string='Descripción')
	descripcion_fr = fields.Text(string='Description')
	descripcion_en = fields.Text(string='Description')
	tipo = fields.Char(string="Tipo")
	sub_tipo = fields.Char(string="Sub-tipo")
	tipo_arq = fields.Char(string="Tipo arquitéctonico")
	es_datasheet_es = fields.Boolean(string = 'Ficha técnica')
	datasheet_es = fields.Binary(string="Ficha técnica")
	datasheet_filename_es = fields.Char(string="Nombre de archivo")
	es_datasheet_fr = fields.Boolean(string = 'Fiche technique')
	datasheet_fr = fields.Binary(string="Fiche technique")
	datasheet_filename_fr = fields.Char(string="Nom du fichier")
	es_datasheet_en = fields.Boolean(string = 'Datasheet')
	datasheet_en = fields.Binary(string="Datasheet")
	datasheet_filename_en = fields.Char(string="File name")
	car_alto = fields.Float(string="Alto(cm)")
	car_ancho = fields.Float(string="Ancho(cm)")
	car_largo = fields.Float(string="Largo(cm)")
	car_peso = fields.Float(string="Peso(kg)")
	superficie = fields.Float(string="Superficie (cm2)",compute="_sup_basic",stored=True)
	@api.onchange('car_ancho','car_largo')
	def _sup_basic(self):
		cm_superficie = self.car_ancho * self.car_largo
		self.superficie = cm_superficie/10000
	ubicacion = fields.Selection(selection=[
	('suelo','suelo'),
	('mural','mural'),
	('sobremesa','sobremesa'),
	],
	string = 'Ubicación predeterminada'
	)
	movilidad = fields.Boolean(string="¿Tiene el equipo una ubicación fija?", default=True)
	fijacion = fields.Boolean(string="¿Necesita el equipo alguna fijación especial?", default=False)
	estructura = fields.Boolean(string="¿Necesita el equipamiento de cambios constructivos en la estructura?", default=False)
	conex_agua = fields.Boolean(string="¿Necesita el equipo conexión a circuito de agua corriente?", default=False)
	conex_tta = fields.Boolean(string="¿Necesita el equipo conexión a circuito de agua especial?", default=False)
	conex_elect = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico corriente?", default=False)
 	#conex_ups = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico de emergencia?", default=False)
	conex_com = fields.Boolean(string="¿Necesita el equipo conexión a red de comunicaciones?", default=False)
	conex_ups = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico de emergencia?", default=False)

