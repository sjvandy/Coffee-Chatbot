#!/usr/bin/env python3
#Steven Vandegrift 2022
import json
orderDatabase = {}
keepRunning = True

print('Welcome to the order archives')

with open('DrinkDatabase.json') as drinkDatabase:
	orderDatabase = json.load(drinkDatabase)

orderAmount = len(orderDatabase['orders'])
print(f'There are {orderAmount} orders in the system')

def clearDatabase():
	with open('DrinkDatabase.json', 'w') as drinkDatabase:
		emptyDatasheet = {'orders': []}
		json.dump(emptyDatasheet, drinkDatabase)

while keepRunning:
	command = input().lower()
	if 'quit' in command:
		keepRunning = False
	elif 'orders' in command:
		print(orderDatabase['orders'])
	elif 'stats' in command:
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
	elif 'delete' in command:
		res = input("YOU ARE ABOUT TO DELETE THE ENTIRE DATABASE, TO VERIFY THIS DECISION, PRESS 'y' TO CONTINUE WITH DELETION. PRESS ANY OTHER KEY OR JUST PRESS ENTER TO ESCAPE")
		if res == 'y':
			clearDatabase()
			