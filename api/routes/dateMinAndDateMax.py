from flask import jsonify
from data import sales

def dateMinAndDateMax():
  return jsonify({
    'dateMin':sales[-1]['date_closed'][:10],
    'dateMax':sales[0]['date_closed'][:10]
    })