from flask import request, jsonify
from data import salesGroupByCategories, sales
from binarySearchIndex import bbinaria_index_mayor_a, bbinaria_index_menor_a

def salesByCategories():
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  dateStart = request.args.get('date_start',False)
  dateEnd = request.args.get('date_end',False)
  if(not dateStart):
    return jsonify(salesGroupByCategories)
  
  indexElementStart = bbinaria_index_mayor_a(sales,dateStart)
  indexElementEnd = bbinaria_index_menor_a(sales,dateEnd)
  salesFiltered = sales[indexElementEnd:indexElementStart + 1] #invertido ya que la lista está ordenada de mayor a menor
  
  filteredsalesGroupByCategories = {}
  for sale in salesFiltered:
    for product in sale['products']:
      if not filteredsalesGroupByCategories.get(product['category'].lower()):
        filteredsalesGroupByCategories[product['category'].lower()] = {
          'total quantities':product['quantity'],
          'total incomes':product['quantity'] * product['price'],
        }
      else:
        filteredsalesGroupByCategories[product['category'].lower()]['total quantities'] += product['quantity']
        filteredsalesGroupByCategories[product['category'].lower()]['total incomes'] += product['quantity'] * product['price']
  return jsonify(filteredsalesGroupByCategories)