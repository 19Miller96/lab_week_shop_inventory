from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    products = manufacturer_repository.products(manufacturer)
    return render_template("manufacturers/show.html", manufacturer = manufacturer, products = products)

@manufacturers_blueprint.route("/manufacturers/<id>/products")
def product_list(id):
    products = manufacturer_repository.products(id)
    return render_template("manufacturers/products.html", products = products)

# Create a new manufacturer here
@manufacturers_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    manufacturer_id = request.form['manufacturer_id']
    product_id = request.form['product_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = product_repository.select(product_id)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", products = products, manufacturers = manufacturers)