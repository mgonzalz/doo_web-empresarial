# Entrega Proyecto Web Empresa.

Este proyecto consiste en el desarrollo de una página web para una empresa utilizando el framework **Django**. El proyecto está compuesto por varias aplicaciones, cada una con una funcionalidad específica:

- **Core**: para gestionar las páginas estáticas (portada, historia y visítanos).
- **Services**: para gestionar los servicios que ofrece la empresa.
- **Blog**: para gestionar las entradas y sus categorías.
- **Social**: para manejar los enlaces a las redes sociales en el pie de página.
- **Pages**: para gestionar las páginas secundarias del pie de página.
- **Contact**: para manejar el formulario de contacto y enviar un email con el mensaje.

Además, el proyecto está desplegado en **Vercel** y tiene un contenedor **Docker** configurado para ejecutar el proyecto en local.

## Repositorio.
- Link: [https://github.com/mgonzalz/doo_web-personal.git](https://github.com/mgonzalz/doo_web-personal.git)
- Usuario: María González - [@mgonzalz](https://github.com/mgonzalz)
- Despliegue en Vercel: [https://doo-web-empresarial-omega.vercel.app/](https://doo-web-empresarial-omega.vercel.app/)

## Estructura del Proyecto.

```python
.
├── manage.py
├── requirements.txt
├── webempresa/                  # Carpeta principal de configuración del proyecto.
│   ├── webempresa/              # Configuración del proyecto Django.
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── ...
│   ├── core/                    # Aplicación para la gestión de las páginas estáticas.
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── ...
│   ├── services/                # Aplicación para la gestión de los servicios ofrecidos.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── blog/                    # Aplicación para la gestión del blog y sus categorías.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── social/                  # Aplicación para la gestión de los enlaces a redes sociales.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── pages/                   # Aplicación para la gestión de las páginas secundarias.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── contact/                 # Aplicación la gestión del formulario de contacto.
│       ├── forms.py
│       ├── views.py
│       ├── ...
│
│   # Configuración de Docker para ejecutar el proyecto localmente.
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
│
├── resources/                   # Plantillas HTML y recursos estáticos.
│   ├── index.html
│   ├── services.html
│   ├── ...
```

- **Core**: Aplicación para gestionar páginas estáticas.
- **Services**: Aplicación para gestionar los servicios de la empresa, que se visualizan en la sección "Servicios".
- **Blog**: Aplicación para administrar las entradas del blog y las categorías relacionadas.
- **Social**: Aplicación que maneja los enlaces a redes sociales que se muestran en el pie de página.
- **Pages**: Aplicación para gestionar las páginas secundarias del pie de página (términos y condiciones, política de privacidad, etc.).
- **Contact**: Aplicación para gestionar el formulario de contacto y enviar los mensajes por correo electrónico.

Además, el proyecto incluye un contenedor **Docker** para facilitar la ejecución local, y se ha configurado un despliegue automático en **Vercel**.

## Instalación.

### Creación de un Entorno Virtual.

Primero, crea un entorno virtual llamado `env-django`:

```bash
python -m venv env-django
env-django\Scripts\activate
```

- Nota: Si usas **VSCode**, puedes necesitar configurar permisos antes de activar el entorno: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

Una vez que el entorno virtual esté activado, instala las dependencias:

```bash
pip install -r requirements.txt
```

### Configuración de Docker.

Si se prefiere ejecutar el proyecto en local con Docker, puede consultar el archivo `DockerSetUp.md` para una guía detallada sobre cómo configurar y ejecutar el proyecto usando Docker.

### Migración de la Base de Datos y Ejecución del Servidor.

Para aplicar las migraciones y ejecutar el servidor de desarrollo, usa los siguientes comandos:

```bash
cd webempresa
python manage.py migrate
python manage.py runserver
```

Una vez hecho esto, abre tu navegador y accede a **http://127.0.0.1:8000/** para ver la página de inicio. Para acceder al panel de administración de Django, ve a **http://127.0.0.1:8000/admin** e ingresa con las credenciales del superusuario.

## Despliegue en Vercel.

El proyecto está configurado para desplegarse automáticamente en **Vercel**. Cualquier cambio realizado en el repositorio se despliega automáticamente a través de la integración con Vercel. Puedes ver el sitio en producción en [https://doo-web-empresarial-omega.vercel.app/](https://doo-web-empresarial-omega.vercel.app/).
