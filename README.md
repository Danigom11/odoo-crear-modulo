# 🌍 Eco-Log: Módulo de Economía Circular para Odoo

Bienvenido al equipo de desarrollo. Este proyecto tiene como objetivo crear un módulo para Odoo 19 que gestione la trazabilidad de residuos y certifique el impacto positivo (ahorro de CO2 y agua).

---

## 🚀 Flujo de Trabajo (LEER IMPORTANTE)

Usamos un tablero Kanban en la pestaña "Projects" de GitHub.
1.  **Pendiente:** Tickets pendientes. Coge uno y muévelo a...
2.  **En Desarrollo:** Estás trabajando en ello. **Solo 1 ticket por persona a la vez.**
3.  **En Revisión:** Ya has terminado el código y has hecho el Pull Request.
4.  **Completado:** Dani (Lead) ha revisado tu código y lo ha fusionado.

---

## 🛠️ Guía Rápida para Desarrolladores

### 1. Preparar tu entorno (Solo la primera vez)

1.  Abre **Visual Studio Code**.
2.  Abre la terminal integrada (`Ctrl + ñ` o *Ver > Terminal*).
3.  Ejecuta este comando para descargar el proyecto:
    ```bash
    git clone [https://github.com/Danigom11/odoo-crear-modulo.git](https://github.com/Danigom11/odoo-crear-modulo.git)
    ```
4.  Ve a *Archivo > Abrir Carpeta* y selecciona la carpeta `odoo-crear-modulo` (o `economia_circular`) que se acaba de descargar.

### 2. Empezar a trabajar (Cada día)

Tus ramas ya están creadas. Antes de escribir nada, **asegúrate de estar en tu rama**:

1.  En la terminal de VS Code, escribe:
    ```bash
    git checkout nombre_de_tu_rama
    ```
    *(Sustituye `nombre_de_tu_rama` por tu nombre, ej: `git checkout maria`).*
2.  Ahora ya puedes empezar a programar (crear archivos en `models/`, `views/`, etc).

### 3. Guardar cambios y subirlos (Desde VS Code)

No hace falta usar comandos complicados. Usa la interfaz de VS Code:

1.  Guarda tus archivos (`Ctrl + S`).
2.  Haz clic en el icono de **"Control de código fuente"** en la barra izquierda (el dibujo de las 3 bolitas conectadas o un grafo).
3.  Escribe un mensaje en el cuadro de texto (ej: "Ticket 2 terminado: Modelo registro").
4.  Dale al botón azul **Confirmar** (o *Commit*).
5.  Dale al botón **Sincronizar cambios** (o *Sync/Push*).

### 4. Entregar el trabajo (Pull Request)

Cuando hayas terminado tu ticket y subido los cambios:

1.  Ve a la página del repositorio en GitHub.
2.  Verás un aviso amarillo arriba que dice que tu rama tiene cambios recientes.
3.  Haz clic en el botón verde **"Compare & pull request"**.
4.  Escribe un título descriptivo y dale a **Create pull request**.
5.  Avisa a Dani para que lo revise.
6.  Mueve tu ticket en el tablero a la columna **In Review**.

---

## 📂 Estructura de Archivos

Para que el puzle encaje, respetad esta estructura:

* `models/`: Aquí van los archivos `.py` (Lógica y Bases de datos).
* `views/`: Aquí van los archivos `.xml` (Formularios, Listas, Menús).
* `security/`: Permisos de acceso.
* `__manifest__.py`: El archivo principal que conecta todo.

---

## 🤖 ¿Qué tengo que hacer? (Tus Instrucciones)

Ve al archivo `PLAN_MAESTRO.md` en este repositorio. Ahí encontrarás:
1.  Tu ticket asignado.
2.  El **Prompt exacto** que debes copiar y pegar en tu IA (ChatGPT/Gemini/DeepSeek).
3.  Copia el código que te dé la IA y crea los archivos correspondientes en VS Code.

> **⚠️ REGLA DE ORO:** No cambies los nombres técnicos de las variables (ej: `tipo_id`, `co2_factor`). Si los cambias, el código de tus compañeros no conectará con el tuyo y el módulo explotará.

¡A programar! 👨‍💻👩‍💻
