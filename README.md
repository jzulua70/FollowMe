# FollowMe

Aplicación de internet de las cosas para tópicos especiales en telemática, Universidad Eafit.

Esta aplicación permite que un usuario pueda crear una cuenta y ser seguido mediante localización GPS a partir de un dispositivo electrónico. De esta manera, el usuario podra ver la ruta que tomó recientemente de manera privada, observandola detalladamente en un mapa. 

# Desarrollo e instalación:

1. La implementación de este proyecto se realizó en los siguientes ambientes:

- Desarrollo: El desarrollo de esta aplicación se llevó a cabo en linux-ubuntu 16.04 lts, utilizando como lenguaje de programación python3.5 y como framework de desarrollo Django 2.0. La base de datos utilizada es Postgres SQL, y se probó en el servidor que traía el django por defecto.

1.1. La base de datos cuenta con los siguientes modelos y relaciones:

1.1.1. auth_user:

                                     Table "public.auth_user"
|Column    |           Type           |                       Modifiers                        |
|-------------|--------------------------|--------------------------------------------------------|
|id           | integer                  | not null default nextval('auth_user_id_seq'::regclass) |
|password     | character varying(128)   | not null                                               |
|last_login   | timestamp with time zone |                                                        |
|is_superuser | boolean                  | not null                                               |
|username     | character varying(150)   | not null                                               |
|first_name   | character varying(30)    | not null                                               |
|last_name    | character varying(150)   | not null                                               |
|email        | character varying(254)   | not null                                               |
|is_staff     | boolean                  | not null                                               |
|is_active    | boolean                  | not null                                               |
|date_joined  | timestamp with time zone | not null                                               |

1.1.2. geoApp_waypoint:

                     Table "public.geoApp_waypoint"
|Column  |         Type          |                           Modifiers                           | 
|----------|-----------------------|--------------------------------------------------------------|
|id       | integer               | not null default nextval('"geoApp_waypoint_id_seq"'::regclass)|
|name     | character varying(32) | not null                                                      |
|geometry | geometry(Point,4326)  | not null                                                      |
|user_id  | integer               | not null                                                      |
|date     | character varying(32) | not null                                                      |
|hour     | character varying(32) | not null                                                      |




1.2. REST Routes:


	   1.2.1 Descripción: Iniciar Sesión
       Método: GET
       URI: /FollowMeApp/login_view
       Representación de datos:
         Datos Response:
             * Datos HTML: Formulario de acceso

 	   1.2.2 Descripción: Cerrar sesión
       Método: GET
       URI: /FollowMeApp/logout
       Representación de datos:
         * Datos Request:
            email:
            password:


	    1.2.3 Descripción: nuevo usuario
        Método: GET
        URI: /FollowMeApp/register
        Representación de datos:
        Datos Response:
            * Datos HTML: Formulario de registro

        1.2.4 Descripción: Obtener posición
        Método: POST
        URI:/geoApp/getData
        Representación de datos:
        	Datos request:
        	-latitud.
        	-longitud.
        	-Hora.
        	-Fecha.
        	-Precisión.

- Test: DCA ubicado en la universidad EAFIT. Se requiere de una VPN para el acceso a la plataforma. El link de acceso es el siguiente (http://10.131.137.230:80/FollowMeApp/index)

- Producción: https://followmee.herokuapp.com/FollowMeApp/index

Para montar la aplicación a heroku se utilizó el siguiente tutorial de la documentación oficial de heroku: (https://devcenter.heroku.com/articles/deploying-python)


2. Especifícaciones técnicas:

	- Python3.5

	- Django2.0

3. Desplegando la aplicación de django en linux Centos 7:
Source: (https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-centos-7)

- Para acceder al sevidor se hace por medio de ssh, con el usario y la ip: user1@10.131.137.230

Luego de acceder las siguientes instalaciones son necesarias:

*Todas las instalaciones se hacen con sudo*.

	-Instalar GitHub: yum install git

	Estas instalaciones son necesarias para que django puede correr correctamente:

	-Instalar python3.5: yum -y install python35u

	-Instalar pip3.5: yum -y install python35u-pip

	-Instalar django: pip3.5 install Django

	-Instalar django-crispy-forms: pip3.5 install django-crispy-forms

	-install dj_database_url: pip3.5 install dj_database_url

	-install psycopg2: pip3.5 install psycopg2

	-instalar whitenoise: pip3.5 install whitenoise

	-Instalar postgis: yum install postgis.

	-Instalar wsgi para python3.5: yum install python35u-mod_wsgi

	-Instalar postgres y crear base de datos:

	-Agregar repositorio Epel: yum -y install epel-release

	-Instalar Postgres: yum install postgresql-server postgresql-contrib postgresql-devel

	- Crear base de datos inicial: sudo postgresql-setup initdb

		-run postgres:

			-sudo systemctl start postgresql

			-sudo systemctl enable postgresql

	- Crear base de datos-FollowMe:

		-sudo -i -u postgres

		-CREATE DATABASE FollowMe WITH OWNER admin;

- Abrir el firewall para el puerto 80: $ sudo firewall-cmd --zone=public --add-port=80/tcp --permanent $ sudo firewall-cmd --reload

-Clonar el repositorio de git e instalarlo:
	
	$ cd /var/www/

	$git clone https://github.com/jzulua70/FollowMe.git

	$cd FollowMe

	$python3.5 manage.py migrate

	$python3.5 manage.py runserver


4. Desplegando en Apache server:

	- source: (https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-centos-7)

	- Instalar httpd: sudo yum install httpd mod_wsgi

	- Para configurar el servidor se edita el siguiente archivo : 

		$sudo nano /etc/httpd/conf.d/django.conf
		con la siguiente información:

		<VirtualHost *:80>                                                                                                                             
		    #My site Name                                                                                                                                           
		    #Demon process for multiple virtual hosts                                                                                                  
		    WSGIDaemonProcess FollowMe python-path=/usr/bin/python3.5                                                                                  
		                                                                                                                                               
		    #Pointing wsgi script to config file                                                                                                       
		    WSGIScriptAlias / /var/www/FollowMe/django.wsgi                                                                                            
		    WSGIProcessGroup FollowMe                                                                                                                  
		                                                                                                                                               
		    #Your static files location                                                                                                                
		    Alias /static/ "/var/www/FollowMe/FollowMeApp/static/"                                                                                     
		    <Location "/media">                                                                                                                        
		        SetHandler None                                                                                                                        
		    </Location>                                                                                                                                
		    <LocationMatch "\.(jpg|gif|png|js|css)$">                                                                                                  
		        SetHandler None                                                                                                                        
		    </LocationMatch>                                                                                                                           
		    <Directory /var/www/FollowMe>                                                                                                              
		        WSGIProcessGroup FollowMe                                                                                                              
		        WSGIApplicationGroup %{GLOBAL}                                                                                                         
		        Order deny,allow                                                                                                                       
		        Allow from all                                                                                                                         
		    </Directory>                                                                                                                               
		</VirtualHost>   

	- Agregar el apache user y darle permisos:

	  $sudo usermod -a -G user1 apache

	  $chmod 710 /home/user


	- Luego comenzamos el servicio de apache:

		$sudo systemctl start httpd

    - Y por último lo habilitamos:

		$sudo systemctl enable httpd








		

 	








