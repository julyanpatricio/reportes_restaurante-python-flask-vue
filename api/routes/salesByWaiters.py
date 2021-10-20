from flask import request, jsonify
from data import salesGroupByWaiter

def salesByWaiters():
  waiter = request.args.get('waiter_name',False)
  limit = request.args.get('limit',10)
  page = request.args.get('page',0)
  if(waiter):
    return jsonify({
      'name':waiter,
      'saled products':salesGroupByWaiter[waiter]['saled products'],
      'total income for sales':salesGroupByWaiter[waiter]['total income for sales'],
      'products':salesGroupByWaiter[waiter]['products'][(int(page)*limit):(limit*(int(page)+1))]
      })
  return jsonify(salesGroupByWaiter)