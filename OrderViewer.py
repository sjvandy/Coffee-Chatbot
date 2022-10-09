#!/usr/bin/env python3
#Steven Vandegrift 2022
import json
orderDatabase = {}

with open('DrinkDatabase.json') as drinkDatabase:
	orderDatabase = json.load(drinkDatabase)

orderAmount = len(orderDatabase['orders'])
print(f'There are {orderAmount} orders in the system')

