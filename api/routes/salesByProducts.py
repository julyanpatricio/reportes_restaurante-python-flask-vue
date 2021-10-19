from flask import request, jsonify
from data import salesGroupByProducts

def salesByProducts():
  product = request.args.get('product_name',False)
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  if(product):
    return jsonify({
      'total quantities':salesGroupByProducts[product]['total quantities'],
      'total incomes':salesGroupByProducts[product]['total incomes'],
      'products':salesGroupByProducts[product]['products'][(page*limit):(limit*(page+1))]
      })
  return jsonify(salesGroupByProducts)
