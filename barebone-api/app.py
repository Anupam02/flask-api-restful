from flask import Flask, jsonify , request, render_template

app = Flask(__name__)

stores = [
    {
        'name': "Anupam's Store",
        'items': [
            {
                'name': 'Mobile',
                'price': 10000.00
            },
            {
                'name': 'Bag',
                'price': 600.00
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store), 201


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name: str):
    # Iterate over get_stores
    # If the store name matches, return it
    # If name match, return an error message
    for store in stores:
        if name == store['name']:
            return jsonify(store), 200
    return jsonify({'message': f'{name} not found in stores'}, 404)


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}), 200

# POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name: str):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item), 200
    return jsonify({'message': f'{store} is not in the store'}, 404)


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': f'{store} not found in stores'}, 404)

app.run(port=5000, debug=True)
