from odoo import models, fields, api

class EconomiaRegistro(models.Model):
    _name = 'economia.registro'
    _description = 'Registro de Economía Circular'
    name = fields.Char(string='Referencia', required=True, default='Nuevo')
    descripcion = fields.Text(string='Detalles del residuo/envase')
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    tipo_id = fields.Selection([
        ('vidrio', 'Vidrio'),
        ('plastico', 'Plástico'),
        ('metal', 'Metal'),
        ('carton', 'Cartón'),
        ('organico', 'Orgánico'),
    ], string='Tipo de Residuo', required=True)
    cantidad = fields.Float(string='Cantidad (kg)', required=True)
    impacto_co2 = fields.Float(string='Impacto CO2 (kg)', compute='_compute_impactos', store=True)
    impacto_agua = fields.Float(string='Agua Ahorrada (litros)', compute='_compute_impactos', store=True)
    
    @api.depends('tipo_id', 'cantidad')
    def _compute_impactos(self):
        # Factores de impacto por tipo de material
        factores_co2 = {
            'vidrio': 0.5,
            'plastico': 2.0,
            'metal': 1.5,
            'carton': 0.8,
            'organico': 0.3,
        }
        factores_agua = {
            'vidrio': 10,
            'plastico': 50,
            'metal': 30,
            'carton': 20,
            'organico': 5,
        }
        for record in self:
            if record.tipo_id and record.cantidad:
                record.impacto_co2 = record.cantidad * factores_co2.get(record.tipo_id, 0)
                record.impacto_agua = record.cantidad * factores_agua.get(record.tipo_id, 0)
            else:
                record.impacto_co2 = 0
                record.impacto_agua = 0


class EconomiaTipoResiduo(models.Model):
    _name = 'economia.tipo_residuo'
    _description = 'Tipo de Residuo/Material'
    _rec_name = 'name'
    
    name = fields.Char(string='Nombre del Material', required=True)
    unidad = fields.Selection([
        ('kg', 'Kilogramos'),
        ('litros', 'Litros')
    ], string='Unidad', default='kg', required=True)
    co2_por_unidad = fields.Float(
        string='CO2 ahorrado por unidad',
        help='Kg de CO2 ahorrados por cada unidad de este material'
    )
    agua_ahorrada = fields.Float(
        string='Agua ahorrada',
        help='Litros de agua ahorrados'
    )
    image = fields.Binary(string='Imagen del Material', attachment=True)
