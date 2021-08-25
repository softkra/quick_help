# quick_help test
### Los commits recientes son agregados por la rama master
### Para hacer el despliegue se necesita que la maquina anfitrión tenga instalado y configurado docker y docker-compose
## Clonar repositorio
- git clone https://github.com/softkra/quick_help.git
#### *No deberia presentar problemas al momento de clonarlo ya que el repositorio es publico*
## Iniciar despliegue del proyecto mediante docker
- Una vez clonado el repositorio, se ingresa al directorio  'quick_help'
- Con `docker-compose up --build -d` se iniciará la contruccion de los contenedores docker que estan configurados para trabajar con la version de Python 3.9 y la ultima de Django soportada por la version de python
- Una vez se creen los contenedores se puede hacer seguimiento a los logs con el comando `docker-compose logs -f` y en este apartado nos debe mostrar lo siguiente:
```
django_1  | Watching for file changes with StatReloader
django_1  | Performing system checks...
django_1  | 
django_1  | System check identified no issues (0 silenced).
django_1  | August 25, 2021 - 05:12:35
django_1  | Django version 3.2.6, using settings 'quick.settings'
django_1  | Starting development server at http://0.0.0.0:8080/
django_1  | Quit the server with CONTROL-C.
```
- Ya el despliegue estaria completo y listo para hacer uso de las apis
- Ahora debemos crear un superusuario para hacer el primer registro y obtencion de token, lo cual se hace con el siguiente comando `docker-compose run django python3 manage.py createsuperuser`, le solicitará un nombre de usuario, email y contraseña
###### La creacion de este usuario se hace por este medio ya que las apis tienen una validacion de token que solo permite ejecutar una vez se tenga un usuario, seria irresponsable tener un api que cree usuarios sin pedir ningun token de autorización 
## Uso de apis
1. Modulo de usuarios
  - `localhost:8080/api/add-user/`: Creacion de nuevos usuarios
    - Parametros POST: email, password
  - `localhost:8080/get_token/`: Obtener token de autenticación
    - Parametros POST: username, password
2. Modulo de Productos
  - `localhost:8080/api/add-product/`: Creacion de nuevos productos
    - Parametros POST: name, description, attribute
  - `localhost:8080/api/detail-product/1/`: Ver detalle de un producto
    - Parametros GET: id producto
  - `localhost:8080/api/delete-product/1/`: Elimina un producto
    - Parametros GET: id producto
  - `localhost:8080/api/update-product/1/`: Modicifación de productos
    - Parametros GET: id producto
    - Parametros POST: name, description, attribute
3. Modulo de Clientes
  - `localhost:8080/api/add-client/`: Creacion de nuevos clientes
    - Parametros POST: document, first_name, last_name, email
  - `localhost:8080/api/detail-client/1/`: Ver detalle de un cliente
    - Parametros GET: id cliente
  - `localhost:8080/api/delete-client/1/`: Elimina un cliente
    - Parametros GET: id cliente
  - `localhost:8080/api/update-client/1/`: Modificación de productos
    - Parametros GET: id cliente
    - Parametros POST: document, first_name, last_name, email
4. Modulo de Facturas
  - `localhost:8080/api/add-bill/`: Creacion de facturas
    - Parametros POST: client_id, company_name, nit, code
  - `localhost:8080/api/detail-bill/1/`: Ver detalle de una facturas
    - Parametros GET: id factura
  - `localhost:8080/api/delete-bill/1/`: Elimina una facturas
    - Parametros GET: id factura
  - `localhost:8080/api/update-bill/1/`: Modificación de facturas
    - Parametros GET: id factura
    - Parametros POST: client_id, company_name, nit, code
5. Modulo de Facturación de productos
  - `localhost:8080/api/add-bill-product/`: Agrega nueva facturacion
    - Parametros POST: bill_id, product_id
  - `localhost:8080/api/detail-bill-product/1/`: Ver detalle de la facturacion
    - Parametros GET: id facturacion
  - `localhost:8080/api/delete-bill-product/1/`: Elimina una facturacion
    - Parametros GET: id facturacion
  - `localhost:8080/api/update-bill-product/1/`: Modificación de la facturacion
    - Parametros GET: id facturacion
    - Parametros POST: bill_id, product_id
6. Modulo para manejo de clientes por archivos CSV
  - `localhost:8080/api/client-report/`: Genera un reporte CSV con la siguiente estructura:
  ```
  Documento,Nombre completo,Facturas relacionadas
  12545555,christian porres,1
  12548965,julio sanchez,0
  524163,roberto galindo,0
  ```
  - `localhost:8080/api/csv-clients/`: Recibe un archivo CSV con información de los clientes y crea los registros
    - Parametros POST: Archivo CSV
    ```
    Estructura de Ejemplo:
      12548965,julio,sanchez,jsanchez@gmail.com
      524163,roberto,galindo,rgalinfo@gmail.com
    ```
### La prueba se sube a un servidor por si se presentan problemas de despliegue, se puede consultar a esta url: `95.216.158.143:8080`
#### Ejemplo: `95.216.158.143:8080/api/client-report`

##### _El código almacenado en este GitHub fue desarrollado por Christian David Porres_
