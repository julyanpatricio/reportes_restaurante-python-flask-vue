from flask import request, jsonify
from data import sales

def _sales():
  limit = int(request.args.get('limit',10))
  page = int(request.args.get('page',0))
  return jsonify({'sales':sales[(page*limit):(limit*(page+1))],'total':len(sales)})
