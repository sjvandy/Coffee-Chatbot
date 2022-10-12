#!/usr/bin/env python3
#Coffee Chatbot Steven Vandegrift 2022
import json
orderDatabase = {}
continueOrdering = True

def loadDatabase():
		try:
			with open('DrinkDatabase.json') as drinkDatabase:
				return json.load(drinkDatabase)
		except:
			pass
		
def uploadToDatabase(database):
	with open('DrinkDatabase.json', 'w') as drinkDatabase:
		json.dump(database, drinkDatabase)

def coffeeBot():
	drink = getDrinkType()
	size = getSize()
	print(f"Alright, that's one {size} {drink} coming up!")
	name = input("What's the name for this order?\n").lower()
	print(f"Thank you {name.title()}, your drink will be ready shortly!")
	order = {
		'customer': name,
		'drink_type': drink,
		'drink_size': size
	}
	return order
	

def getSize(size = 'none'):
	if size == 'none':
		properResponce = False
		res = input('What size? \nSmall, Medium, or Large\n').lower()
		while not properResponce:
			if 'small' in res:
				properResponce
				return 'small'
			elif 'medium' in res:
				return 'medium'
			elif 'large' in res:
				return 'large'
			else:
				res = input("hmmm, that doesn't appear to be an option, what size do you want?\n").lower()
	

def getDrinkType():
	properResponce = False
	res = input('What kind of drink would you like?\nWe have "Brewed Coffee", "Mocha", or a "Latte"\n').lower()
	while not properResponce:
		if 'mocha' in res:
			return 'mocha'
		elif 'latte' in res:
			if 'vanilla' in res:
				if '2%' in res or 'regular' in res or 'normal' in res:
					return orderLatte('vanilla', '2%')
				elif 'non' in res or 'fat' in res:
					return orderLatte('vanilla', 'non-fat')
				elif 'soy' in res:
					return orderLatte('vanilla', 'soy')
				else:
					return orderLatte('vanilla')
			elif 'chocolate' in res:
				if '2%' in res or 'regular' in res or 'normal' in res:
					return orderLatte('chocolate', '2%')
				elif 'non' in res or 'fat' in res:
					return orderLatte('chocolate', 'non-fat')
				elif 'soy' in res:
					return orderLatte('chocolate', 'soy')
				else:
					return orderLatte('chocolate')
			elif 'caramel' in res:
				if '2%' in res or 'regular' in res or 'normal' in res:
					return orderLatte('caramel', '2%')
				elif 'non' in res or 'fat' in res:
					return orderLatte('caramel', 'non-fat')
				elif 'soy' in res:
					return orderLatte('caramel', 'soy')
				else:
					return orderLatte('caramel')
			else:
				return orderLatte()
		elif 'brewed' in res or 'coffee' in res:
			return 'brewed coffee'
		else:
			res = input("Sorry, but we don't serve that kind of coffee here, what would you like instead?\n").lower()


def orderLatte(flavor = 'none', milk = 'none'):
	if flavor == 'none':
		properResponce = False
		while not properResponce:
			flavor = input("What flavor? 'Chocolate, Vanilla, or Caramel?\n").lower()
			if 'vanilla' in flavor:
				flavor = 'vanilla'
				properResponce = True
			elif 'chocolate' in flavor:
				flavor = 'chocolate'
				properResponce = True
			elif 'caramel' in flavor:
				flavor = 'caramel'
				properResponce = True
			else:
				flavor = input("Sorry, it can only be one of the three flavors here, which one would you like?\n").lower()
	if milk == 'none':
		properResponce = False
		while not properResponce:
			milk = input("Now what kind of milk do you want in your latte?\nWe have 2%, Non-fat, and soy milk\n").lower()
			if 'non' in milk or 'fat' in milk:
				milk = 'non-fat'
				properResponce = True
			elif 'soy' in milk:
				milk = 'soy'
				properResponce = True
			elif '2%' in milk or 'normal' in milk or 'regular' in milk:
				milk = '2%'
				properResponce = True
			else:
				milk = input('Sorry, we do not carry that kind of milk, please select from the following\n').lower()
	return f'{milk} {flavor} latte'

def requestAnotherOrder():
	responce = input('Would you like to make another order? "yes" or "no"\n').lower()
	if 'no' in responce:
		return False
	elif 'yes' in responce:
		return True
	else:
		print('if statement was ignored')

print("Welcome to the cafe")
while continueOrdering == True:
	orderDatabase = loadDatabase()
	coffeeObject = coffeeBot()
	orderDatabase['orders'].append(coffeeObject)
	uploadToDatabase(orderDatabase)
	continueOrdering = requestAnotherOrder()