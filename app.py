from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importa a classe de configuração
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados usando a classe Config
app.config.from_object(Config)
login_manager = LoginManager()
# Inicializando o SQLAlchemy com a configuração do Flask
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

#User BD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=True)
    cart = db.relationship('CartItem', backref='user', lazy=True)

# Definição do modelo Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# LOGIN AUTETICATE
@app.route('/login', methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(username=data.get("username")).first()
    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Logged in sucessfully"})
    return jsonify({"message": "unauthorized, Invalid credentials"}), 401

@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout in sucessfully"})

@app.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
     data = request.json
     if 'name' in data and  'price' in data:
        product = Product(name=data["name"],price=data["price"],description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added sucessfully"}), 200
     return jsonify({"message": "Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted sucessfully"}), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/products/<int:product_id>', methods=["GET"])
@login_required
def get_produxt_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"messagem": "Product Not Found"}), 404


@app.route('/api/products', methods=["GET"])
@login_required
def get_all():
    products = Product.query.all()  # Busca todos os produtos
    print(products)
    product_list= []
    for product in products:
        print(product)
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }
        product_list.append(product_data)

    return jsonify(product_list)

    
    # return jsonify({"message": "No products found"}), 404


@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
@login_required
def update_products(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "No products found"}), 404

    data = request.json
    if 'name' in data:
        product.name = data['name']

    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.price = data['description']

    db.session.commit()
    return jsonify({"message": "Product Updated sucessfully"})

# Chekout
@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = User.query.get(int(current_user.id))
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id,product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Item added to cart sucessfully!"})
    return jsonify({"message": "Failed to add item to cart"}), 400

@app.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Item removed from the cart sucessfully"})
    return jsonify({"message":"Failed to remove item from the cart"}),400

@app.route('/api/cart', methods=['GET'])
@login_required
def view_cart():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    cart_content = []
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        user_teste = User.query.get(cart_item.user_id)
        cart_content.append({
            "id": cart_item.id,
            # "user_id": cart_item.user_id,
            "user_id": user_teste.id,
            "user_name": user_teste.username,
            "product_id": product.id,
            "product_name": product.name,
            "product_price": product.price
        })

    return jsonify(cart_content)

@app.route('/api/cart/checkout', methods=["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    for cart_item in cart_items:
        db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"message": "Checkout sucessfully. Cart has been cleared"})


# Rota simples para a página inicial
@app.route('/')
def hello_world():
    return 'Hello World'

# Criação das tabelas e execução da aplicação
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Criar todas as tabelas no banco de dados

    app.run(debug=True)
