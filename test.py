from app import  app , db
import unittest


class APPTesting(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code , 200)
    
    def test_get_products_id(self):
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code , 200)
    
    def test_create_product(self):
        data = {
        'title': 'New Product',
        'description': 'Description of the new product',
        'price': 10.99
        }
        response = self.app.post('/products', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        product_id = 1
        data = {
        'title': 'Updated Product',
        'description': 'Updated description',
        'price': 19.99
        }
        response = self.app.put(f'/products/{product_id}', json=data)
        self.assertEqual(response.status_code, 200)

def test_delete_product(self):
    product_id = 1
    response = self.app.delete(f'/products/{product_id}')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()