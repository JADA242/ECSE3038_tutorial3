# ECSE3038_tutorial3

## Fast Fruit Inventory API

This FastAPI-based RESTful API manages a Fresh Fruit Inventory System. It allows users to perform CRUD (Create, Read, Update, Delete) operations on fruit inventory data.

## Endpoints
GET /api/fruits: Retrieves a list of all available fruits in the inventory.\
GET /api/fruits/{id}: Retrieves detailed information about a specific fruit by its ID.\
POST /api/fruits: Adds a new fruit to the inventory. The creation_date is automatically set.\
PATCH /api/fruits/{id}: Updates the availability, price, or quantity of a specific fruit.\
DELETE /api/fruits/{id}: Marks a fruit as unavailable (soft delete).

## Fruit Model

The fruit object has the following attributes:\
name: Name of the fruit\
variety: Variety of the fruit\
quantity: Quantity in stock\
supplier: Supplier information
harvest_date: Date of harvest\
creation_date: Date of creation (automatically set)\
available: Availability status (true/false)\
price: Price per unit

## Purpose of Code
The purpose of this code is to complete a tutorial for an IOT course.
