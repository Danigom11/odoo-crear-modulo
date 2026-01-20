# Economía Circular - Módulo para Odoo 19

Bienvenido al equipo de desarrollo. Este proyecto tiene como objetivo crear un módulo para Odoo 19 que gestione la trazabilidad de residuos y certifique el impacto positivo (ahorro de CO2 y agua).

Este proyecto ha sido desarrollado por **Daniel Gómez, Daniel del Campo, Álvaro Neculau, Alex Stanila, Martina Valdivia y Víctor Rivera**.

---

## Índice

1. [Información General del Proyecto](#información-general-del-proyecto)
2. [Problemática y Solución](#problemática-y-solución)
3. [Funcionalidades Principales](#funcionalidades-principales)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Tecnologías Utilizadas](#tecnologías-utilizadas)
6. [Modelos de Datos](#modelos-de-datos)
7. [Vistas e Interfaz](#vistas-e-interfaz)
8. [Sistema de Reportes](#sistema-de-reportes)
9. [Seguridad y Permisos](#seguridad-y-permisos)
10. [Instalación y Configuración](#instalación-y-configuración)

---

## Información General del Proyecto

### Descripción
**Economía Circular** es un módulo personalizado para Odoo 19 que permite a las empresas gestionar programas de reciclaje y retorno de materiales, proporcionando trazabilidad completa y certificación del impacto ambiental positivo generado por cada cliente.

### Datos del Proyecto
- **Nombre del Módulo**: `economia_circular` (Economía Circular Velas)
- **Versión**: 1.0
- **Plataforma**: Odoo 19.0
- **Categoría**: Sustainability (Sostenibilidad)
- **Licencia**: LGPL-3
- **Tipo**: Módulo de Aplicación

### Contexto Académico
Este proyecto ha sido desarrollado como trabajo de la asignatura **SGE (Sistemas de Gestión Empresarial)** del curso **2º DAM (Desarrollo de Aplicaciones Multiplataforma)**.

---

## Problemática y Solución

### Problema que Resuelve

Las empresas que implementan programas de economía circular (reciclaje, retorno de envases, reutilización) enfrentan varios desafíos:

1. **Falta de trazabilidad**: No existe un registro centralizado de las contribuciones de reciclaje de cada cliente
2. **Cálculos manuales ineficientes**: El impacto ambiental (CO2, agua) se calcula manualmente, generando errores y consumiendo tiempo
3. **Ausencia de certificación**: Los clientes no reciben reconocimiento formal de su contribución ambiental
4. **Datos dispersos**: La información de sostenibilidad no está integrada con el sistema CRM y ventas de la empresa

### Solución Implementada

Este módulo proporciona:

- **Registro automatizado** de devoluciones de materiales por cliente
- **Cálculo automático** del impacto ambiental (CO2 y agua ahorrados)
- **Generación de certificados PDF** profesionales de sostenibilidad
- **Integración nativa** con el módulo de clientes de Odoo
- **Sistema de validación** con workflow de estados (Borrador → Validado)
- **Gestión de múltiples materiales** con factores de impacto personalizables

---

## Funcionalidades Principales

### 1. Gestión de Tipos de Residuos/Materiales

El módulo permite configurar un catálogo de materiales reciclables con las siguientes características:

- **Nombre del material**: Identificación del tipo de residuo (ej: vidrio, plástico, metal, cartón, orgánico)
- **Unidad de medida**: Kilogramos o Litros
- **Factor de CO2**: Cantidad de CO2 ahorrado por cada unidad de material reciclado
- **Factor de agua**: Litros de agua ahorrados por unidad
- **Imagen**: Representación visual del material

**¿Por qué es importante?**  
Permite personalizar los cálculos según el tipo de negocio y los datos reales de impacto de cada material, adaptándose a diferentes industrias.

### 2. Registro de Economía Circular

Funcionalidad central que permite crear registros individuales de reciclaje con:

- **Referencia única**: Identificador automático del registro
- **Cliente asociado**: Vinculación con el módulo de contactos de Odoo (`res.partner`)
- **Tipo de material**: Selección del material devuelto
- **Cantidad entregada**: Peso o volumen del material
- **Fecha de entrega**: Control temporal de las contribuciones
- **Descripción y notas**: Campos adicionales para contexto
- **Cálculo automático de impacto**:
  - **CO2 ahorrado** = Cantidad × Factor CO2 del material
  - **Agua ahorrada** = Cantidad × Factor Agua del material
- **Estado del registro**: Borrador / Validado (workflow de validación)

**¿Por qué es importante?**  
Centraliza toda la información de reciclaje, elimina cálculos manuales y proporciona datos objetivos del impacto ambiental real.

### 3. Sistema de Workflow con Estados

Implementa un ciclo de vida para cada registro:

- **Estado Borrador**: Registro inicial, permite modificaciones
- **Botón "Validar"**: Confirma el registro y lo marca como oficial
- **Estado Validado**: Registro certificado, listo para generar certificado
- **Botón "Volver a Borrador"**: Permite revertir validaciones si es necesario

**¿Por qué es importante?**  
Proporciona control de calidad y trazabilidad, evitando cambios accidentales en registros certificados.

### 4. Visualización Avanzada de Impactos

Utiliza widgets visuales tipo "gauge" (indicadores circulares) para mostrar:

- Impacto de CO2 en tiempo real
- Impacto de agua en tiempo real
- Actualización automática al cambiar cantidad o tipo de material

**¿Por qué es importante?**  
Facilita la comprensión inmediata del impacto ambiental sin necesidad de analizar números.

### 5. Generación de Certificados de Sostenibilidad

Genera automáticamente certificados PDF profesionales que incluyen:

- Logo de la empresa
- Datos del cliente
- Cantidad y tipo de material reciclado
- Impacto ambiental calculado (CO2 y agua)
- Diseño profesional con formato corporativo
- Descarga e impresión directa desde Odoo

**¿Por qué es importante?**  
Permite a las empresas reconocer formalmente el compromiso ambiental de sus clientes, fomentando la fidelización y el marketing verde.

---

## Estructura del Proyecto

```
odoo-crear-modulo/
│
├── __init__.py                      # Inicialización del módulo Python
├── __manifest__.py                  # Manifiesto de Odoo (configuración del módulo)
├── README.md                        # Documentación del proyecto
│
├── models/                          # Modelos de datos (Lógica de negocio)
│   ├── __init__.py                  # Inicialización de modelos
│   └── economia.py                  # Definición de modelos: EconomiaTipoResiduo y EconomiaRegistro
│
├── views/                           # Vistas XML (Interfaz de usuario)
│   ├── economia_view.xml            # Vistas de formularios, listas y menús para registros
│   └── tipo_residuo_view.xml        # Vistas para gestión de tipos de residuos
│
├── report/                          # Reportes PDF
│   └── certificado_report.xml       # Template del certificado de sostenibilidad
│
└── security/                        # Seguridad y permisos
    └── ir.model.access.csv          # Control de acceso a modelos
```

### Explicación Detallada de Cada Carpeta

#### `__manifest__.py`
**Propósito**: Es el archivo de configuración principal que Odoo lee para instalar el módulo.

**Contenido**:
- Nombre y descripción del módulo
- Versión y autor
- Dependencias de otros módulos (`base`, `sale`)
- Lista de archivos de datos a cargar (vistas, seguridad, reportes)
- Configuración de instalabilidad y tipo de aplicación

**¿Por qué existe?**: Sin este archivo, Odoo no reconocería el directorio como un módulo válido.

#### `models/`
**Propósito**: Contiene la lógica de negocio y la definición de las tablas de base de datos.

**Archivo `economia.py`**:
Define dos modelos principales usando el ORM de Odoo:

1. **`economia.tipo_residuo`**: 
   - Tabla para almacenar los tipos de materiales
   - Campos: nombre, unidad, factores de impacto, imagen
   - Se usa como catálogo maestro

2. **`economia.registro`**:
   - Tabla principal de registros de reciclaje
   - Campos: referencia, cliente, tipo de material, cantidad, fecha, notas, impactos calculados
   - Métodos computados: `_compute_impactos()` calcula automáticamente CO2 y agua
   - Métodos de acción: `action_confirm()` y `action_draft()` para cambiar estados

**¿Por qué existe?**: Separa la lógica de negocio de la presentación, siguiendo el patrón MVC. El ORM de Odoo traduce estos modelos Python a tablas PostgreSQL automáticamente.

#### `views/`
**Propósito**: Define la interfaz de usuario (formularios, listas, menús) en formato XML.

**Archivo `economia_view.xml`**:
- Vista de formulario: Interfaz para crear/editar registros de reciclaje
- Vista de lista (tree): Tabla resumen de todos los registros
- Menús: Estructura de navegación en Odoo
- Acciones: Define qué vista abrir al hacer clic en un menú

**Archivo `tipo_residuo_view.xml`**:
- Vistas para gestionar el catálogo de materiales
- Formulario simplificado para configuración de tipos

**¿Por qué existe?**: Odoo utiliza XML para declarar la interfaz de usuario de forma estructurada y reutilizable.

#### `report/`
**Propósito**: Contiene las plantillas QWeb para generar reportes PDF.

**Archivo `certificado_report.xml`**:
- Define la acción del reporte (qué modelo, qué tipo)
- Template HTML/QWeb con el diseño del certificado
- Utiliza variables dinámicas para datos del registro
- Estilos CSS inline para el formato PDF

**¿Por qué existe?**: Permite generar documentos PDF profesionales directamente desde Odoo usando datos del registro.

#### `security/`
**Propósito**: Controla quién puede acceder y modificar los datos.

**Archivo `ir.model.access.csv`**:
- Define permisos de lectura, escritura, creación y eliminación
- Configura acceso por grupos de usuarios
- En este caso, otorga permisos completos a usuarios base

**¿Por qué existe?**: Es obligatorio en Odoo para que el módulo funcione. Sin permisos definidos, nadie podría acceder a los datos.

---

## Tecnologías Utilizadas

### Backend
- **Python 3.10+**: Lenguaje de programación para la lógica de negocio
- **Odoo ORM**: Sistema de mapeo objeto-relacional para interactuar con la base de datos
- **PostgreSQL**: Base de datos relacional (manejada automáticamente por Odoo)

### Frontend
- **XML**: Declaración de vistas e interfaces
- **QWeb**: Motor de plantillas de Odoo para renderizado HTML/PDF
- **JavaScript (Odoo Web Framework)**: Widgets y comportamientos interactivos

### Módulos de Odoo Utilizados
- **base**: Módulo fundamental de Odoo (modelos de contactos, usuarios, etc.)
- **sale**: Módulo de ventas (integración con clientes)

### Herramientas de Desarrollo
- **Git/GitHub**: Control de versiones y colaboración
- **Visual Studio Code**: Editor de código
- **Odoo Development Mode**: Para debugging y testing

---

## Modelos de Datos

### Modelo 1: `economia.tipo_residuo`

**Tabla**: `economia_tipo_residuo`

| Campo | Tipo | Descripción | Requerido | Valor por Defecto |
|-------|------|-------------|-----------|-------------------|
| `name` | Char | Nombre del material | Sí | - |
| `unidad` | Selection | Unidad de medida (kg/litros) | Sí | 'kg' |
| `co2_por_unidad` | Float | CO2 ahorrado por unidad | No | 0.0 |
| `agua_ahorrada` | Float | Agua ahorrada por unidad | No | 0.0 |
| `image` | Binary | Imagen del material | No | - |

**Relaciones**:
- Relación One2Many implícita con `economia.registro` (un tipo puede tener muchos registros)

**¿Cómo funciona?**  
Actúa como tabla maestra de configuración. Los factores de impacto se multiplican por la cantidad en cada registro para calcular el impacto total.

### Modelo 2: `economia.registro`

**Tabla**: `economia_registro`

| Campo | Tipo | Descripción | Requerido | Valor por Defecto |
|-------|------|-------------|-----------|-------------------|
| `name` | Char | Referencia del registro | Sí | 'Nuevo' |
| `descripcion` | Text | Detalles del residuo | No | - |
| `partner_id` | Many2one | Relación con res.partner | Sí | - |
| `tipo_id` | Many2one | Relación con tipo_residuo | Sí | - |
| `cantidad` | Float | Cantidad entregada | Sí | 0.0 |
| `fecha` | Date | Fecha del registro | No | Hoy |
| `notas` | Text | Notas adicionales | No | - |
| `impacto_co2` | Float | CO2 calculado (computed) | No | Calculado |
| `impacto_agua` | Float | Agua calculada (computed) | No | Calculado |
| `state` | Selection | Estado (draft/confirmed) | No | 'draft' |

**Relaciones**:
- `partner_id`: Many2One con `res.partner` (clientes de Odoo)
- `tipo_id`: Many2One con `economia.tipo_residuo` (tipo de material)

**Campos Computados**:
```python
@api.depends('cantidad', 'tipo_id.co2_por_unidad', 'tipo_id.agua_ahorrada')
def _compute_impactos(self):
    # Se ejecuta automáticamente cuando cambia cantidad o tipo
    impacto_co2 = cantidad × factor_co2_del_tipo
    impacto_agua = cantidad × factor_agua_del_tipo
```

**¿Cómo funciona?**  
Cada vez que se cambia la cantidad o el tipo de material, Odoo recalcula automáticamente los impactos ambientales usando el decorador `@api.depends`.

---

## Vistas e Interfaz

### Vista de Formulario (Form View)

**Componentes**:

1. **Header**: 
   - Botones de acción (Validar, Volver a Borrador)
   - Widget statusbar para mostrar el estado actual

2. **Sheet (Cuerpo)**:
   - **Grupo izquierdo**: Datos del registro (nombre, cliente, tipo, fecha)
   - **Grupo derecho**: Cantidad, estado, indicadores gauge de impacto
   - **Sección inferior**: Descripción y notas (campos de texto largo)

**Elementos Visuales Destacados**:
- **Ribbon "CERTIFICADO"**: Aparece solo cuando el estado es "Validado"
- **Widgets Gauge**: Medidores circulares visuales para CO2 y agua
- **Botones contextuales**: Cambian según el estado (visibilidad condicional con `attrs`)

### Vista de Lista (Tree View)

Muestra tabla resumen con columnas:
- Referencia
- Cliente
- Tipo de material
- Cantidad
- Fecha
- Impacto CO2
- Impacto Agua
- Estado

Permite ordenar, filtrar y buscar rápidamente todos los registros.

Capturas del módulo real en funcionamiento:
<img width="1914" height="315" alt="image" src="https://github.com/user-attachments/assets/7cb2ec33-32f9-46b7-b1f6-12cc369f6818" />

<img width="1524" height="810" alt="image" src="https://github.com/user-attachments/assets/44d3906e-f82e-4b35-8586-3b319ca42d86" />

<img width="1077" height="859" alt="image" src="https://github.com/user-attachments/assets/3725e74f-10e0-43c4-b08f-854f02abe5be" />


### Menús

Estructura de navegación:
```
Sostenibilidad (Menú raíz)
├── Registros de Economía Circular
└── Tipos de Residuos (Configuración)
```

---

## Sistema de Reportes

### Certificado de Sostenibilidad

**Trigger**: Botón "Imprimir → Certificado de Impacto Positivo" en el formulario de registro

**Proceso**:
1. Usuario hace clic en "Imprimir"
2. Odoo ejecuta la acción `ir.actions.report`
3. Se renderiza el template QWeb con datos del registro
4. Se genera un PDF con estilo profesional
5. Se descarga automáticamente

**Contenido del Certificado**:
- Logo de la empresa (si está configurado)
- Nombre del cliente
- Título: "CERTIFICADO DE SOSTENIBILIDAD"
- Texto de agradecimiento personalizado
- Cantidad y tipo de material reciclado
- Métricas de impacto (CO2 y agua ahorrados)
- Fecha de emisión
- Diseño con colores corporativos (verde para sostenibilidad)

**Código de ejemplo (extracto)**:
```xml
<p class="lead">
    Gracias a la gestión de <strong><span t-field="o.cantidad"/> kg</strong> de 
    <strong><span t-field="o.tipo_id"/></strong>,
    has generado este impacto positivo:
</p>
```

---

## Seguridad y Permisos

### Archivo `ir.model.access.csv`

Define reglas de acceso a nivel de modelo:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_economia_registro,economia.registro,model_economia_registro,base.group_user,1,1,1,1
access_economia_tipo_residuo,economia.tipo_residuo,model_economia_tipo_residuo,base.group_user,1,1,1,1
```

**Explicación**:
- `perm_read=1`: Los usuarios pueden **leer** registros
- `perm_write=1`: Los usuarios pueden **modificar** registros
- `perm_create=1`: Los usuarios pueden **crear** nuevos registros
- `perm_unlink=1`: Los usuarios pueden **eliminar** registros
- `group_id=base.group_user`: Se aplica a todos los usuarios internos de Odoo

**¿Por qué es crítico?**  
Sin estos permisos definidos, Odoo bloqueará el acceso a los modelos por seguridad, mostrando errores de "Access Denied".

---

## Instalación y Configuración

### Requisitos Previos
- Odoo 19.0 instalado
- PostgreSQL funcionando
- Módulos base y sale instalados

### Pasos de Instalación

1. **Copiar el módulo**:
   ```bash
   cp -r economia_circular /path/to/odoo/addons/
   ```

2. **Actualizar lista de aplicaciones**:
   - Ir a Aplicaciones en Odoo
   - Clic en "Actualizar lista de aplicaciones"

3. **Instalar el módulo**:
   - Buscar "Economía Circular"
   - Clic en "Instalar"

4. **Configurar tipos de residuos**:
   - Ir a Sostenibilidad → Tipos de Residuos
   - Crear materiales (vidrio, plástico, etc.) con sus factores de impacto

5. **Crear registros**:
   - Ir a Sostenibilidad → Registros de Economía Circular
   - Clic en "Crear" y completar formulario

6. **Generar certificados**:
   - Abrir un registro validado
   - Clic en Imprimir → Certificado de Impacto Positivo

---

## Conclusión

Este módulo demuestra conocimientos en:

- Desarrollo de módulos personalizados en Odoo
- Modelado de datos con ORM
- Creación de vistas XML complejas
- Implementación de lógica de negocio con Python
- Generación de reportes PDF con QWeb
- Gestión de seguridad y permisos
- Integración con módulos nativos de Odoo
- Trabajo colaborativo con Git/GitHub
- Documentación técnica completa

El proyecto resuelve una necesidad real de sostenibilidad empresarial, proporcionando una solución técnica completa y funcional que puede ser utilizada en entornos de producción reales.
