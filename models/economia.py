from odoo import models, fields


class EconomiaRegistro(models.Model):
    _name = 'economia.registro'
    _description = 'Registro de Economía Circular'

    name = fields.Char(string='Referencia', required=True, default='Nuevo')
    descripcion = fields.Text(string='Detalles del residuo/envase')
    state = fields.Selection(
        [('draft', 'Borrador'), ('confirmed', 'Validado')],
        string='Estado',
        default='draft',
        tracking=True,
    )

    def action_confirm(self):
        """Cambia el estado a confirmado"""
        self.write({'state': 'confirmed'})

    def action_draft(self):
        """Devuelve el estado a borrador"""
        self.write({'state': 'draft'})


class EconomiaTipoResiduo(models.Model):
    _name = 'economia.tipo_residuo'
    _description = 'Tipo de Residuo/Material'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Material', required=True)
    unidad = fields.Selection(
        [('kg', 'Kilogramos'), ('litros', 'Litros')],
        string='Unidad',
        default='kg',
        required=True,
    )
    co2_por_unidad = fields.Float(
        string='CO2 ahorrado por unidad',
        help='Kg de CO2 ahorrados por cada unidad de este material',
    )
    agua_ahorrada = fields.Float(
        string='Agua ahorrada',
        help='Litros de agua ahorrados',
    )
    image = fields.Binary(string='Imagen del Material', attachment=True)
