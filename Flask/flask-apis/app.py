from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

# Sample in-memory database (for demonstration)
items = [
    {"id": 1, "name": "item1", "description": "This is item 1"},
    {"id": 2, "name": "item2", "description": "This is item 2"}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# GET an item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# POST a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1  # simple ID assignment
    items.append(new_item)
    return jsonify(new_item), 201

# PUT (update) an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# DELETE an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
