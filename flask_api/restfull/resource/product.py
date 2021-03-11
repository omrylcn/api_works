from flask import request
from flask_restful import Resource
from http import HTTPStatus

from model.product import Product, product_list


class ProductListResource(Resource):

    def get(self):
        
        data = []

        for product in product_list:
            if product.is_publish is True:
                data.append(product.data)

        return {"data": data}, HTTPStatus.OK
        

    def post(self):

        data = request.get_json()

        product = Product(id=data["id"],
                          category_id=data["category_id"],
                          product_name=data["product_name"],
                          quantity_per_unit=data["quantity_per_unit"],
                          unit_price=data["unit_price"],
                          units_in_stock=data["units_in_stock"])

        product_list.append(product)

        return recipe.data, HTTPStatus.CREATED
