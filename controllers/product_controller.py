from flask import Flask, render_template, request, redirect
from flask import Blueprint

import pdb

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

@products_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", manufacturers = manufacturers)

# Create a new product here
@products_blueprint.route("/products",  methods=['POST'])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_cost = request.form["selling_cost"]
    manufacturer = request.form["manufacturer"]
    new_product = Product(name, description, stock_quantity, buying_cost, selling_cost, manufacturer)
    product_repository.save(new_product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
