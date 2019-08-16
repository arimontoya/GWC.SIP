#This Code generates a randomized chipotle order for the user
#Created by Arianna Montoya

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
meal_type = ["a Bowl", "a Salad", "a Burrito", "Tacos"]
meat = ["Chicken", "Steak", "Sofritas", "Carnitas", "Barbacoa"]
rice = ["White Rice", "Brown Rice"]
beans = ["Brown Beans", "Black Beans"]
salsa = ["Pico de Gallo", "Corn Salsa", "Green Salsa", "Red Salsa"]
toppings = ["Cheese", "Lettuce", "Guacamole", "Sour Cream"]

#Generates a random integer.
random_meal = randint(0, len(meal_type)-1)
random_rice = randint(0, len(rice)-1)
random_beans = randint(0, len(beans)-1)
random_meat = randint(0, len(meat)-1)
random_salsa = randint(0, len(salsa)-1)
random_toppings = randint(0, len(salsa)-1)
                    

print ("Your new Chipotle order is " + (meal_type[random_meal]) + " with " + (rice[random_rice]) + ", " + (beans[random_beans]) + ", " + (meat[random_meat]) + ", " + (salsa[random_salsa]) + ", and " + (toppings[random_toppings]) + ".")
