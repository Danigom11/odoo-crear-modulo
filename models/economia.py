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
        tracking=True
    )
    
    def action_confirm(self):
        """Cambia el estado a confirmado"""
        self.write({'state': 'confirmed'})
    
    def action_draft(self):
        """Devuelve el estado a borrador"""
        self.write({'state': 'draft'})