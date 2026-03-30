from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "T-Shirt", "price": 500},
    {"id": 2, "name": "Jeans", "price": 1200},
    {"id": 3, "name": "Shoes", "price": 2000}
]

cart = []

# HTML + JS inside Python
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Online Shop</title>
</head>
<body>

<h1>🛒 Simple Online Shop</h1>

<h2>Products</h2>
<ul id="products"></ul>

<h2>Cart</h2>
<ul id="cart"></ul>

<script>
function loadProducts() {
    fetch('/api/products')
    .then(res => res.json())
    .then(data => {
        let p = document.getElementById("products");
        p.innerHTML = "";
        data.forEach(item => {
            p.innerHTML += `<li>
                ${item.name} - ₹${item.price}
                <button onclick="addToCart(${item.id})">Add</button>
            </li>`;
        });
    });
}

function loadCart() {
    fetch('/api/cart')
    .then(res => res.json())
    .then(data => {
        let c = document.getElementById("cart");
        c.innerHTML = "";
        data.forEach(item => {
            c.innerHTML += `<li>${item.name} - ₹${item.price}</li>`;
        });
    });
}

function addToCart(id) {
    fetch('/api/cart', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id})
    })
    .then(() => {
        loadCart();
    });
}

loadProducts();
loadCart();
</script>

</body>
</html>
"""

# Home page
@app.route('/')
def home():
    return render_template_string(html_page)

# Get products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get cart
@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

# Add to cart
@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product = next((p for p in products if p["id"] == data["id"]), None)
    if product:
        cart.append(product)
        return jsonify({"message": "Added to cart"})
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)