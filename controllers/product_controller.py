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

@products_blueprint.route("/products/new", methods=['GET'])
def create_new_product():
    products = product_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/net.html", products = products, manufacturers = manufacturers)

