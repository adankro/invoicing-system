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

 - Initialize the database

```
- $VENV/bin/initialize_invoicing_db development.ini
 ```

 - start development server 

 ```
- $VENV/bin/pserve development.ini
 ```

 Current db schema:
----------------------------------------------
 ![alt text](https://github.com/adankro/invoicing-system/blob/dev/images/current_db.png?raw=true)


Testing API endpoints
-------------------------------------------------

- Create

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

 ``` url
POST http://localhost:8000/invoice_item
 ```

Content-Type: application/json

json body example :

```json
{
      "id":1,
      "invoice_id": 1,
      "description": "PlayStation 5",
      "amount":2000,
      "units":2

 }
 ```

- Quey data

``` url
GET http://localhost:8000/invoice
 ```

``` url
GET http://localhost:8000/invoice_item
 ```

