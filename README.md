# LeWorkConstructora

LeWorkConstructora es una aplicación web diseñada para mostrar información sobre una empresa constructora, incluyendo sus proyectos, servicios, información de contacto y detalles sobre la empresa.  Permite a los visitantes explorar los proyectos completados, conocer los servicios ofrecidos y contactar a la empresa para consultas.

## Características Principales

* **core:** Gestiona las funcionalidades principales del sitio, como la página de inicio y el formulario de contacto.
* **projects:** Administra los detalles de los proyectos, incluyendo imágenes y categorías.
* **services:** Maneja las descripciones de los servicios y su categorización.
* **about:** Contiene información sobre la empresa, el equipo y testimonios.


## Guía de Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1. **Clonar el Repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd LeWorkConstructora
   ```

2. **Crear un Entorno Virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Linux/macOS
   .venv\Scripts\activate  # En Windows
   ```

3. **Instalar las Dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar las Migraciones de la Base de Datos:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un Superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el Servidor de Desarrollo:**
   ```bash
   python manage.py runserver
   ```

Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes URLs:

* **Panel de Administración:** `/admin/`
* **Página de Inicio:** `/`
* **Listado de Proyectos:** `/projects/`
* **Detalle de Proyecto:** `/projects/<id_del_proyecto>/` (reemplaza `<id_del_proyecto>` con el ID real)
* **Listado de Servicios:** `/services/`
* **Detalle de Servicio:** `/services/<id_del_servicio>/` (reemplaza `<id_del_servicio>` con el ID real)
* **Acerca de Nosotros:** `/about/`
* **Contacto:** `/contact/`
