# Aplicacion Web De Tareas Pendientes

Este es un proyecto de aplicación web creado con Django para gestionar tareas pendientes. La aplicación permite a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre las tareas, con el fin de organizar sus actividades y pendientes.

## Características

- CRUD de Tareas: Permite a los usuarios agregar, ver, actualizar y eliminar tareas.
- Interfaz amigable: Diseño sencillo y funcional para facilitar la administración de las tareas.
- Modelo de Datos: Organiza la información de cada tarea con campos como nombre, descripción, estado, y fecha de vencimiento.

## Tecnologías Utilizadas
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: SQLite (por defecto en Django, puede ser reemplazado por otras bases de datos)

## Instalación
### Prerrequisitos
Asegúrate de tener instalado Python y pip.
1. Clona el repositorio:
```bash
git clone https://github.com/alonso1298/Aplicacion-Web-De-Tareas-Pendientes.git
```
2. Navega al directorio del proyecto:
```bash 
cd Aplicacion-Web-De-Tareas-Pendientes
```

3. Instala las dependencias:
```bash 
pip install -r requirements.txt
```

4. Realiza las migraciones de la base de datos:
```bash 
python manage.py migrate
```

5. Ejecuta el servidor de desarrollo:
```bash 
python manage.py runserver
```

## Uso
1. Desde la página de inicio, puedes ver todas las tareas pendientes.
2. Usa el botón "Agregar Tarea" para crear una nueva tarea.
3. Haz clic en "Editar" para modificar una tarea existente o en "Eliminar" para borrarla.

## Estructura del Proyecto
- **app_tareas/**: Carpeta principal de la aplicación de tareas.
- **templates/**: Archivos HTML de la interfaz de usuario.
- **static/**: Archivos CSS y JavaScript para el frontend.
- **models.py**: Define el modelo de datos para la aplicación.
- **views.py**: Contiene las vistas de Django para gestionar las tareas.

## Contribución

1. Haz un fork del proyecto.
2. Crea una rama nueva para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -m 'Agrega nueva funcionalidad').
4. Sube los cambios a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.