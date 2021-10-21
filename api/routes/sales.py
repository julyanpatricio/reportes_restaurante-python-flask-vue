from flask import request, jsonify
from data import sales
from binarySearchIndex import bbinaria_index_mayor_a, bbinaria_index_menor_a

def _sales():
  limit = int(request.args.get('limit',10))
  page = int(request.args.get('page',0))
  dateStart = request.args.get('date_start',False)
  dateEnd = request.args.get('date_end',False)
  if(not dateStart):
    return jsonify({
    'sales':sales[(page*limit):(limit*(page+1))],
    'total':len(sales),
    'dateMin':sales[-1]['date_closed'][:10],
    'dateMax':sales[0]['date_closed'][:10]
    })
  
  indexElementStart = bbinaria_index_mayor_a(sales,dateStart)
  indexElementEnd = bbinaria_index_menor_a(sales,dateEnd)
  salesFiltered = sales[indexElementEnd:indexElementStart + 1] #invertido ya que la lista está ordenada de mayor a menor
  return jsonify({
    'sales':salesFiltered[(page*limit):(limit*(page+1))],
    'total':len(salesFiltered),
    'dateMin':sales[-1]['date_closed'][:10],
    'dateMax':sales[0]['date_closed'][:10]
    })