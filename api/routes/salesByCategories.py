from flask import request, jsonify
from data import salesGroupByCategories

def salesByCategories():
  category = request.args.get('category_name',False)
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  if(category):
    return jsonify({
      'name':category,
      'total quantities':salesGroupByCategories[category]['total quantities'],
      'total incomes':salesGroupByCategories[category]['total incomes'],
      'products':salesGroupByCategories[category]['products'][(int(page)*limit):(limit*(int(page)+1))]
      })
  return jsonify(salesGroupByCategories)