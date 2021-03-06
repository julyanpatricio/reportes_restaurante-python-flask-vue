from flask import Flask 
import json
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

if __name__ == '__main__':
  from routes.dateMinAndDateMax import dateMinAndDateMax
  from routes.sales import _sales
  from routes.salesByCategories import salesByCategories
  from routes.salesByProducts import salesByProducts
  from routes.salesByWaiters import salesByWaiters
  from routes.saleById import saleById

  app.add_url_rule('/date_min_and_date_max', view_func=dateMinAndDateMax)
  app.add_url_rule('/sales', view_func=_sales)
  app.add_url_rule('/sales/categories', view_func=salesByCategories)
  app.add_url_rule('/sales/products', view_func=salesByProducts)
  app.add_url_rule('/sales/waiters', view_func=salesByWaiters)
  app.add_url_rule('/sale/<string:id>', view_func=saleById)
  app.run(debug=True, port=4000)

