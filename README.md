# Aplicación de Reserva de Servicios

## Requisitos

- Python 3.8 o superior
- Git

## Instalación

Antes que nada, abra una terminal en su sistema operativo. En Windows, puede ser `cmd` o `powershell`. En Linux, generalmente `bash`, pero el "*emulador de terminal*" (el que hace uso de `bash`) puede ser *Konsole*, *GNOME Terminal*, *Terminator*, etc. En macOS, *Terminal*.

### 1. Clonar el repositorio

```bash
git clone https://github.com/alkemyTech/CFITDF-Django-W2-Back-S3.git
cd CFITDF-Django-W2-Back-S3
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Cambiar al directorio del proyecto
```bash
cd WebApp
```

### 5. Aplicar migraciones
Esto crea las tablas y estructuras necesarias para que la aplicación funcione correctamente
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
Esto permitirá, finalmente, acceder a la aplicación
```bash
python manage.py runserver
```

### 8. Uso
Una vez el servidor esté corriendo, puede acceder a la aplicación en el navegador, ingresando a:
http://127.0.0.1:8000/

Y al panel de administración:
http://127.0.0.1:8000/admin/
