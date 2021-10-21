from flask import request, jsonify
from data import salesGroupByWaiter, sales
from binarySearchIndex import bbinaria_index_mayor_a, bbinaria_index_menor_a

def salesByWaiters():
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  dateStart = request.args.get('date_start',False)
  dateEnd = request.args.get('date_end',False)

  if(not dateStart):
    return jsonify(salesGroupByWaiter)
  
  indexElementStart = bbinaria_index_mayor_a(sales,dateStart)
  indexElementEnd = bbinaria_index_menor_a(sales,dateEnd)
  salesFiltered = sales[indexElementEnd:indexElementStart + 1] #invertido ya que la lista está ordenada de mayor a menor
  
  filteredsalesGroupByWaiters = {}
  for sale in salesFiltered:
    for product in sale['products']:
      if not filteredsalesGroupByWaiters.get(sale['waiter'].lower()):
        filteredsalesGroupByWaiters[sale['waiter'].lower()] = {
        'saled products':product['quantity'],
        'total income for sales':product['quantity'] * product['price'],
      }
    else:
      filteredsalesGroupByWaiters[sale['waiter'].lower()]['saled products'] += product['quantity']
      filteredsalesGroupByWaiters[sale['waiter'].lower()]['total income for sales'] += product['quantity'] * product['price']
    
  return jsonify(filteredsalesGroupByWaiters)