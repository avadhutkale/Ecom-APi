from flask import Flask , jsonify , request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(200))
    price=db.Column(db.Float,nullable=False)

    def __repr__(self):
        return f'<Product Id={self.id},Product Title="{self.title}">'

with app.app_context():
    db.create_all()

@app.route('/products',methods = ['GET'])
def get_products():
    products = Product.query.all()
    products_list=[]

    for  product in products:
        product_dict={

            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        }
        products_list.append(product_dict)
    return jsonify(products_list)

@app.route('/products/<int:id>',methods = ['GET'])
def get_product(id):
    product=Product.query.get_or_404(id)
    product_Dict={
        'id': product.id,
        'title':product.title,
        'description':product.description,
        'price':product.price
    }
    return jsonify(product_Dict)

@app.route('/products',methods = ['POST'])
def create_product():
    try:
        data = request.get_json()
        product = Product(title=data['title'], description=data['description'], price=data['price'])
        db.session.add(product)
        db.session.commit()

        Product_details = {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        }

        response = jsonify(Product_details)
        response.status_code = 201
        return response
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:id>', methods = ['PUT'])
def update_product(id):
    try:
        data = request.get_json()
        product = Product.query.get_or_404(id)
        product.title = data['title']
        product.description = data['description']
        product.price = data['price']
        db.session.commit()
        return jsonify({
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        })
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:id>', methods = ['DELETE'])
def delete_product(id):
    prod = Product.query.get_or_404(id)
    db.session.delete(prod)
    db.session.commit()
    return '',204

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}) , 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'Error' : 'server error could not response to the request'}) , 500

