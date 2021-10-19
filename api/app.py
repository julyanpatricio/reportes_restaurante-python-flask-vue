from flask import Flask, jsonify, request
import json, requests
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

if __name__ == '__main__':
  from routes.home import home
  from routes.sales import _sales
  from routes.salesByCategories import salesByCategories
  from routes.salesByProducts import salesByProducts
  from routes.saleById import saleById

  app.add_url_rule('/home', view_func=home)
  app.add_url_rule('/sales', view_func=_sales)
  app.add_url_rule('/sales/categories', view_func=salesByCategories)
  app.add_url_rule('/sales/products', view_func=salesByProducts)
  app.add_url_rule('/sale/<string:id>', view_func=saleById)
  app.run(debug=True, port=4000)

