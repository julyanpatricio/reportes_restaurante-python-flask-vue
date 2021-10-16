from flask import request, jsonify
from data import sales

def saleById(id):
  sale = list(filter(lambda sale: sale['id'] == id, sales))
  if(len(sale)):
    return jsonify({'sale':sale[0]})
  return  jsonify({'error':'not found'})