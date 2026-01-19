from odoo import models, fields, api


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


class EconomiaRegistro(models.Model):
    _name = 'economia.registro'
    _description = 'Registro de Economía Circular'

    name = fields.Char(string='Referencia', required=True, default='Nuevo')
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    tipo_id = fields.Many2one('economia.tipo_residuo', string='Tipo de Residuo', required=True)
    cantidad = fields.Float(string='Cantidad Entregada', required=True, default=0.0)
    fecha = fields.Date(string='Fecha', default=fields.Date.today)
    descripcion = fields.Text(string='Detalles del residuo/envase')
    notas = fields.Text(string='Notas')
    impacto_co2 = fields.Float(
        string='Impacto CO2 (kg)',
        compute='_compute_impactos',
        store=True,
        readonly=True,
    )
    impacto_agua = fields.Float(
        string='Impacto Agua (litros)',
        compute='_compute_impactos',
        store=True,
        readonly=True,
    )
    state = fields.Selection(
        [('draft', 'Borrador'), ('confirmed', 'Validado')],
        string='Estado',
        default='draft',
        tracking=True,
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

    def action_confirm(self):
        """Cambia el estado a confirmado."""
        self.write({'state': 'confirmed'})

    def action_draft(self):
        """Devuelve el estado a borrador."""
        self.write({'state': 'draft'})
