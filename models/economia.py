from odoo import models, fields

class TipoResiduo(models.Model):
    _name = 'economia.tipo_residuo'
    _description = 'Tipo de Residuo'
    name = fields.Char(string='Nombre', required=True)

class EconomiaRegistro(models.Model):
    _name = 'economia.registro'
    _description = 'Registro de Entregas de Residuos'
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    tipo_id = fields.Many2one('economia.tipo_residuo', string='Tipo de Residuo', required=True)
    cantidad = fields.Float(string='Cantidad Entregada')
    fecha = fields.Date(string='Fecha', default=fields.Date.today)
    notas = fields.Text(string='Notas')