#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    ammounts = {}
    for i in recipe:
        if i in list(ingredients.keys()):
            ammounts[i] = ingredients[i] // recipe[i]
        else:
            return 0
    min_batches = min(list(ammounts.values()))
    if min_batches < 1:
        return 0
    else:
        return min_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
