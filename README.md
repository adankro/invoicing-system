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
      "description": "playtation 5",
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


Questions
-------------------------------------------------

 1. If we wanted to keep track of who needs to pay the invoice, and who needs to get paid for the invoice, how would you extend the application?

- I would add a new model for the invoce vendor and another for the invoice customer, these two models will have a primary key like an id and the additional details like tax_id, name, address, email and phone that will be related as a foreign key on the invoice entity.

 ![alt text](https://github.com/adankro/invoicing-system/blob/dev/images/add_tables.png?raw=true)


2. This project used a relational database. Would you recommend using a NoSQL database instead? Why?

- No, the current aproach of using a relational database looks good so far. Because the data model is very normalized and structured, it is hard to say we need to use a NoSQL database instead until we do a deep analisys about what kind of data is going to fill the model and the main use of this information.

- For example, if this data will be used for data analisys and we need to create a datalake, I would probably use the NoSQL approach to kill the time that a denormalization takes for datalakes formation.

- Another good reason to change this to a Nosql model is if the main use will be to create and query the complete invoices all the time and have a API endpoint to support upload and query the complete documents.

3. If we had to add some tests to this project, but we had limited time, what would you do?

- Create integration testing to englobe several components and use cases.

- Use a parametrized unit test for those cases that are  repetitive use cases such as in a model CRUD for REST API.
