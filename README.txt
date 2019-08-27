Instalar Python
	https://www.python.org/downloads/
Instalar git
	https://git-scm.com/downloads
Clonar
	cmd $ git clone https://github.com/SrSharly/Repo_Enreda
Activar entorno virtual
	cmd	$ cd repo_enreda/virtualenreda/scripts
	cmd	$ activate
Volver al directorio repo_enreda
	cmd $ cd..
	cmd $ cd..
Migrar base de datos
	cmd	$ python manage.py migrate
Crear superuser
	cmd $ python manage.py createsuperuser
	(insertar nombre/correo/contraseña)
Lanzar servidor
	cmd $ python manage.py runserver
Cargar la pagina en el navegador
	http://127.0.0.1:8000/
Para cargar la tabla usuarios se puede acceder a http://127.0.0.1:8000/admin e ingresar el superuser creado.


*cmd $ = comando a ingresar en la consola de comandos de windows.
** = en consola de comando linux la sintaxis para llamar a "python" será "python3" E.G: python3 manage.py runserver