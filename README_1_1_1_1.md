
# LASAMA - Control de Boletas (Django + PWA)

### 1. Instalar local
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # usuario finanzas
python manage.py runserver

- Movil: http://127.0.0.1:8000/
- Finanzas: http://127.0.0.1:8000/admin/  y  /exportar/

### 2. Subir a la nube (Render.com)
- Sube este proyecto a GitHub
- En Render -> New Web Service -> conecta tu repo
- Build: pip install -r requirements.txt
- Start: gunicorn control_boletas.wsgi --log-file -
- Agrega variable DATABASE_URL (Render Postgres gratis)
- Agrega Cloudinary keys si quieres almacenamiento ilimitado en nube

### 3. Instalación Móvil
- Abre el link de Render en el celular
- Chrome -> 3 puntitos -> Agregar a pantalla de inicio / Instalar app
- Queda como App LASAMA con icono rojo

### Anti-duplicado
Hash SHA256 de imagen + unique constraint. Si suben misma foto 2 veces, rechaza.

### Excel Finanzas
/admin/exportar/ descarga XLSX listo para contabilidad.

Empresa: LASAMA
