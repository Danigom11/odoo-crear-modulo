from odoo import models, fields, api

class EconomiaRegistro(models.Model):
    _name = 'economia.registro'
    _description = 'Registro de Economía Circular'
    name = fields.Char(string='Referencia', required=True, default='Nuevo')
    descripcion = fields.Text(string='Detalles del residuo/envase')
    cantidad = fields.Float(string='Cantidad', required=True, default=0.0)
    tipo_id = fields.Many2one('economia.tipo_residuo', string='Tipo de Residuo', required=True)
    
    # Campos computados
    impacto_co2 = fields.Float(
        string='Impacto CO2 (kg)',
        compute='_compute_impactos',
        store=True,
        readonly=True
    )
    impacto_agua = fields.Float(
        string='Impacto Agua (litros)',
        compute='_compute_impactos',
        store=True,
        readonly=True
    )
    
    @api.depends('cantidad', 'tipo_id.co2_por_unidad', 'tipo_id.agua_ahorrada')
    def _compute_impactos(self):
        for record in self:
            if record.tipo_id:
                record.impacto_co2 = record.cantidad * record.tipo_id.co2_por_unidad
                record.impacto_agua = record.cantidad * record.tipo_id.agua_ahorrada
            else:
                record.impacto_co2 = 0.0
                record.impacto_agua = 0.0


class EconomiaTipoResiduo(models.Model):
    _name = 'economia.tipo_residuo'
    _description = 'Tipo de Residuo'
    
    name = fields.Char(string='Nombre', required=True)
    co2_por_unidad = fields.Float(string='CO2 por Unidad (kg)', default=0.0)
    agua_ahorrada = fields.Float(string='Agua Ahorrada (litros)', default=0.0)