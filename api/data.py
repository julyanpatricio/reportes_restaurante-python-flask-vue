import json, requests

resp = requests.get('https://storage.googleapis.com/backupdatadev/ejercicio/ventas.json')
sales = json.loads(resp.content)


salesGroupByCategories={}
salesGroupByProducts={}
for sale in sales:
  for product in sale['products']:
    if not salesGroupByCategories.get(product['category'].lower()):
      salesGroupByCategories[product['category'].lower()] = {
        'total quantities':product['quantity'],
        'total incomes':product['quantity'] * product['price'],
        'products':[product]
        }
    else:
      salesGroupByCategories[product['category'].lower()]['total quantities'] += product['quantity']
      salesGroupByCategories[product['category'].lower()]['total incomes'] += product['quantity'] * product['price']
      salesGroupByCategories[product['category'].lower()]['products'].append(product)
    
    if not salesGroupByProducts.get(product['name'].lower()):
      salesGroupByProducts[product['name'].lower()] = {
        'total quantities':product['quantity'],
        'total incomes':product['quantity'] * product['price'],
        'products':[product]
        }
    else:
      salesGroupByProducts[product['name'].lower()]['total quantities'] += product['quantity']
      salesGroupByProducts[product['name'].lower()]['total incomes'] += product['quantity'] * product['price']
      salesGroupByProducts[product['name'].lower()]['products'].append(product)
