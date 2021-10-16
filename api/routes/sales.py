from flask import request, jsonify
from data import sales

def _sales():
  name = request.args.get('producto',False)
  category = request.args.get('categoria',False)
  if(name):
    totalQuantity=0
    totalIncome=0
    for sale in sales:
      for product in sale['products']:
        if(product['name'].lower() == name.lower()):
          totalQuantity += product['quantity']
          totalIncome += product['quantity'] * product['price']
    return jsonify({
      'product': name.title(),
      'total quantities': totalQuantity,
      'total income': totalIncome
      })
  elif(category):
    totalQuantity=0
    totalIncome=0
    for sale in sales:
      for product in sale['products']:
        if(product['category'].lower() == category.lower()):
          totalQuantity += product['quantity']
          totalIncome += product['quantity'] * product['price']
    return jsonify({
      'category': category.title(),
      'total quantities': totalQuantity,
      'total income': totalIncome
      })
  return jsonify(sales[:5])
