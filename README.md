# telloChatBackend
Backend

# PASO 1: 
CREAR BASE DE DATOS EN PGADMIN CON LOS MISMOS PARAMETROS QUE SE ENCUENTRAN EN EL ARCHIVO   apichat/secret.json
# PASO 2: 
EJECUTAR EL requirements.txt para que no genere problema de librerias 
# PASO 3: 
Una vez creada la base de datos y ejecutado el requirements.txt se deben ejecutar las migraciones dentro de apichat/  
-> python manage.py makemigrations y despues python manage.py migrate
# PASO 4: 
Cuando Las migraciones se hayan ejecutado correctamente proceder a ejecutar el servidor  python manage.py runserver 
y dejarlo encendido. ---> ir al Front para Configuar e instalar


#IMPORTANTE.....
El programa Funciona con autenticación por TOKEN, y tiene sus respectivos ENDPOINTS creados con RestFramework.
Por cuestion de tiempo y que me encontrabá un poco indispuesto no alcancé a implementar SOCKETS-IO para tener todo en tiempo real y me faltó tambien la carga de imagenes.

# La Autenticación se realiza por medio de cuentas de google y posteriormente en la BD se crean los Tokens necesarios para la implementación

# Las Validaciones por parte del backend estan realizadas correctamente, exigiendo un token para poder generar las peticiones
# Las Validaciones por parte del Front no alcancé a realizarlas completamente.

# Paginacion implementada en Backend Completa OK
# Paginacion implementada en Front Incompleta

# Columna con ultimos usuarios y sus fechas de ingreso OK
# Sala de Chat Publica y con opción de Borrar Mensajes OK
