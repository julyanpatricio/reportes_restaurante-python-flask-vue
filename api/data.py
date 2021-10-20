import json, requests
from orderData import merge_sort

resp = requests.get('https://storage.googleapis.com/backupdatadev/ejercicio/ventas.json')
sales = merge_sort(json.loads(resp.content))



salesGroupByCategories={}
salesGroupByProducts={}
salesGroupByWaiter={}
for sale in sales:
  for product in sale['products']:
    if not salesGroupByCategories.get(product['category'].lower()):
      salesGroupByCategories[product['category'].lower()] = {
        'total quantities':product['quantity'],
        'total incomes':product['quantity'] * product['price'],
        }
    else:
      salesGroupByCategories[product['category'].lower()]['total quantities'] += product['quantity']
      salesGroupByCategories[product['category'].lower()]['total incomes'] += product['quantity'] * product['price']
    
    if not salesGroupByProducts.get(product['name'].lower()):
      salesGroupByProducts[product['name'].lower()] = {
        'total quantities':product['quantity'],
        'total incomes':product['quantity'] * product['price'],
        'category': product['category']
        }
    else:
      salesGroupByProducts[product['name'].lower()]['total quantities'] += product['quantity']
      salesGroupByProducts[product['name'].lower()]['total incomes'] += product['quantity'] * product['price']
    
    if not salesGroupByWaiter.get(sale['waiter'].lower()):
      salesGroupByWaiter[sale['waiter'].lower()] = {
        'saled products':product['quantity'],
        'total income for sales':product['quantity'] * product['price'],
        }
    else:
      salesGroupByWaiter[sale['waiter'].lower()]['saled products'] += product['quantity']
      salesGroupByWaiter[sale['waiter'].lower()]['total income for sales'] += product['quantity'] * product['price']
    
