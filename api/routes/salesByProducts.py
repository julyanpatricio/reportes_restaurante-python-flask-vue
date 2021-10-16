from flask import request, jsonify
from data import salesGroupByProducts

def salesByProducts():
  product = request.args.get('nombre_producto',False)
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  if(product):
    return jsonify(salesGroupByProducts[product])
  return jsonify({
    'total quantities':salesGroupByProducts['total quantities'],
    'total incomes':salesGroupByProducts['total incomes'],
    'products':salesGroupByProducts['products'][(page*limit):(limit*(page+1))]
    })