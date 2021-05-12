# Prueba para Globalbit

(Es necesario primero configurar el repositorio del back end)

## Frontend de la prueba

Para correr el front debe tener instalada una version de python igual o mayor a la 3 
después se debe crear un entorno virtual para instalar las dependencias, 
para ello se pueden usar los siguientes comandos.

Para Windows:
```shell
--python3 -m venv <nombre_del_entorno>
--<nombre_del_entorno>\Scripts\activate.bat
```

Para Linux o MAC:
```shell
--python3 -m venv <nombre_del_entorno>
--source <nombre_del_entorno>/bin/activate
```

una vez hecho se usa el paquete pip para instalar las dependencias:

```shell
pip install -r requirements.txt
```

Se debe posicionar en la carpeta global_front

```shell
cd global_front
```

Ya dentro de la carpeta se puede hacer uso del archivo manage.py para correr el Frontend usando
el framework Django

```shell
python manage.py runserver
```

Con esto el servidor estará corriendo en la ruta http://127.0.0.1:8000.

Ahora como ya se configuró anteriormente el servidor del back end, el front estará listo para realizar
peticiones y consumir los servicios de FastAPI