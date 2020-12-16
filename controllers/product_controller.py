from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    manufacturers = product_repository.manufacturers(product)
    return render_template("products/show.html", product = product, manufacturers = manufacturers)

# Create a new product here
@products_blueprint.route("/products",  methods=['POST'])
def create_product():
    product_id = request.form['product_id']
    manufacturer_id = request.form['manufacturer_id']
    product = product_repository.select(product_id)
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", products = products, manufacturers = manufacturers)

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')

