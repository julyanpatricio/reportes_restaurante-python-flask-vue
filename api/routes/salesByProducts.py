from flask import request, jsonify
from data import salesGroupByProducts, sales
from binarySearchIndex import bbinaria_index_mayor_a, bbinaria_index_menor_a

def salesByProducts():
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  dateStart = request.args.get('date_start',False)
  dateEnd = request.args.get('date_end',False)
  if(not dateStart):
    return jsonify(salesGroupByProducts)
  
  indexElementStart = bbinaria_index_mayor_a(sales,dateStart)
  indexElementEnd = bbinaria_index_menor_a(sales,dateEnd)
  salesFiltered = sales[indexElementEnd:indexElementStart + 1] #invertido ya que la lista está ordenada de mayor a menor
  
  filteredSalesGroupByProducts = {}
  for sale in salesFiltered:
    for product in sale['products']:
      
      if not filteredSalesGroupByProducts.get(product['name'].lower()):
        filteredSalesGroupByProducts[product['name'].lower()] = {
          'total quantities':product['quantity'],
          'total incomes':product['quantity'] * product['price'],
          'category': product['category']
          }
      else:
        filteredSalesGroupByProducts[product['name'].lower()]['total quantities'] += product['quantity']
        filteredSalesGroupByProducts[product['name'].lower()]['total incomes'] += product['quantity'] * product['price']
  return jsonify(filteredSalesGroupByProducts)