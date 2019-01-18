from flask import Flask, jsonify, make_response, request
import json

app = Flask(__name__)
API_URL = "/products/api/v1.0/"

products = None

@app.route("/")
def index():
    print(products)
    return "Sample API"

@app.route(API_URL+"all", methods=['GET'])       #products/api/v1.0/all
def get_all_products():
    return jsonify(products)


@app.route(API_URL+"all/<product>", methods=['GET'])   #products/api/v1.0/all/<product_name>
def get_product(product):
    if product in products:
        return jsonify({product: products[product]})
    return make_response(jsonify({'Error': 'Not Found!'}),404)

@app.route(API_URL+"available", methods=['GET'])         #products/api/v1.0/available
def get_all_available():
    output = {}
    for product in products:
        if products[product]['inventory']>0:
            output[product] = products[product]
    return jsonify(output)

@app.route(API_URL+"available/<product>", methods=['GET'])  #products/api/v1.0/available/<product_name>
def get_available_product(product):
    if product in products:
        if products[product]["inventory"] >0:
            return jsonify({product: products[product]})
    return make_response(jsonify({'Error': 'Not Found!'}),404)

@app.route(API_URL+"purchase", methods=['POST'])            #products/api/v1.0/purchase
def purchase():
    if not request.json or 'product' not in request.json:
        return make_response(jsonify({'Error':'Bad Request! Please read API Docs'}), 400)
    product = request.json['product']
    if product not in products or products[product]['inventory'] < 1:
        return make_response(jsonify({'Error': 'Product Not Found!'}), 404)
    products[product]['inventory'] -=1
    return make_response(jsonify(
        {product: products[product],
         'Message': 'Purchase Successful!'}
    ), 201)

def verify_data():
    for product in products:
        if 'price' not in product or 'inventory' not in product or product['inventory'] < 0:
            return False
    return True

def main():
    with open("products.json", "r") as f:
        global products
        products = json.load(f)

    if not verify_data():
        app.run(debug=True)
    print("Please fix errors in inventory data!!")

if __name__ == "__main__":
    main()

