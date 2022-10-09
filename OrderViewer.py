#!/usr/bin/env python3
#Steven Vandegrift 2022
import json
orderDatabase = {}
keepRunning = True

print('Welcome to the order archives')
print('type "help" for list of commands')

with open('DrinkDatabase.json') as drinkDatabase:
	orderDatabase = json.load(drinkDatabase)

orderAmount = len(orderDatabase['orders'])
print(f'{orderAmount} order(s) found in Database')

def clearDatabase():
	with open('DrinkDatabase.json', 'w') as drinkDatabase:
		emptyDatasheet = {'orders': []}
		json.dump(emptyDatasheet, drinkDatabase)
		print('Database has been deleted.')

while keepRunning:
	command = input().lower()
	if 'quit' in command:
		keepRunning = False
	elif 'view orders' in command:
		if len(orderDatabase['orders']) > 0:
			for order in orderDatabase['orders']:
				print(f"{order['customer']}, 1 {order['drink_size']} {order['drink_type']}")
	elif 'view stats' in command:
		if len(orderDatabase['orders']) == 0:
			print('There are no orders in the database')
			continue
		totalOrders = len(orderDatabase['orders'])
		latteCount = 0
		brewedCount = 0
		mochaCount = 0
		for order in orderDatabase['orders']:
			if 'latte' in order['drink_type']:
				latteCount += 1
			elif 'brewed coffee' in order['drink_type']:
				brewedCount += 1
			elif 'mocha' in order['drink_type']:
				mochaCount += 1
		lattePercent = latteCount/totalOrders
		brewedPercent = brewedCount/totalOrders
		mochaPercent = mochaCount/totalOrders
		print(f"{round(brewedPercent*100)}% of orders are brewed coffee, {round(mochaPercent * 100)}% of orders are Mocha, and {round(lattePercent * 100)}% of orders are Lattes.")
	elif 'delete database' in command:
		res = input("YOU ARE ABOUT TO DELETE THE ENTIRE DATABASE, TO VERIFY THIS DECISION, PRESS 'y' TO CONTINUE WITH DELETION. PRESS ANY OTHER KEY OR JUST PRESS ENTER TO ESCAPE\n")
		if res == 'y':
			clearDatabase()
	elif 'help' in command:
		print('view orders --- shows all orders in database in singular rows')
		print('view stats -------------- shows percentages of drinks ordered')
		print('delete database ------------ resets database back to 0 orders')
		print('quit --------------------------------------- ends the program')