"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        all_products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products = all_products)

    def new(self):
        return self.load_view('add_product.html')

    def edit(self):
        return self.load_view('edit_product.html')

    def show(self):
        pass

    def create(self):
        pass

    def destroy(self):
        pass

    def update(self):
        pass

