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
    return render_template("products/new.html", products = products, manufacturers = manufacturers)

# def create_task():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')

# @visits_blueprint.route("/visits",  methods=['POST'])
# def create_task():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')