invoicing system 

=================================================

A) Running the app using docker and docker compose
-------------------------------------------------

```console
 :$ make build
 ```

```console
 :$ make start
 ```
 or 

```console
:$  docker-compose build
 ```

```console
:$  docker-compose up web 
 ```


B) Running the app using virtualenv or VENV
-------------------------------------------------
-  Install invoice app package
```
$VENV/bin/pip install -e .
 ```

 - 2 Initialize the database

```
- $VENV/bin/initialize_invoicing_db development.ini
 ```

 start development server 
- $VENV/bin/pserve development.ini


Testing API endpoints

Endpoints:
Create
``` url
POST http://localhost:8000/invoice
 ```

Content-Type: application/json

json body example :

```json
{
      "id":1,
      "date": "2020-10-13 22:00:00"
 }
 ```