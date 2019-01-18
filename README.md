#Flask API

##Introduction
This is a simple server-side web API built using python flask. The purpose of this is to be used for reference
for bigger projects. In this API, we model it for an online store with a variable number of products having different prices
and inventory.

##Architecture
Since this is a simple application, it is entirely contained within one file - _app.py_.
The inventory data is stored within *products.json*

Please make sure that _products.json_ contains data in the right format as follows:
1. The file MUST contain a dictionary. This dictionary's keys must be strings, where 
each key refers to a product's name. 
2. For each product, the value is a dictionary. This dictionary MUST contain 2 fields:
    - **price** : The value of this field must be a non-negative float
    - **inventory** : The value of this field must be a non-negative integer

##How to Run
1. Make sure you have python3 installed. Then install all the requirements:
> pip3 install -r requirements.txt


2. Make sure that the *products.json* file is in the same directory as *app.py* and has the correct data format.
3. Run the following command to launch the Flask Application:
> python3 app.py

Now the application will be running at http://localhost:5000
Going to this address should give you the message "Welcome to Flask Sample API!". If this is not the case, that means there was an error 
launching the application. Please check the command prompt.

###Using the API
Now that the application is running we can play around with the api. For this we will use the 'curl' command. This application was tested on 
Windows 10, however, the linux commands should be similar.

- To get all products:
> curl -i http://localhost:5000/products/api/v1.0/all 

- To get a specific product:
> curl -i http://localhost:5000/products/api/v1.0/all/<PRODUCT_NAME>

- To get all available products:
> curl -i http://localhost:5000/products/api/v1.0/available

- To get a specific available product:
> curl -i http://localhost:5000/products/api/v1.0/available/<PRODUCT_NAME>

- To purchase a product:
> curl -i -H "Content-Type: application/json" -X POST -d "{\"product\":\"<PRODUCT_NAME>\"}" http://localhost:5000/products/api/v1.0/purchase
