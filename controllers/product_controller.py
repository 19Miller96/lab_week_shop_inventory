from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@products_blueprint.route("/products/<id>")
def show(id):
    products = product_repository.products(products)
    return render_template("manufacturers/show.html", products = products)
