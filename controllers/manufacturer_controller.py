from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

import pdb

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

@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    name = request.form["name"]
    new_manufacturer = Manufacturer(name)
    manufacturer_repository.save(new_manufacturer)
    return redirect('/manufacturers')
