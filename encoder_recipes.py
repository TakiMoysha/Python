import csv
import json

def encode(args):
    tmp = 0
    for i in args:
        tmp += int(i, 16)
    return tmp


def print_rows():
    with open('Recipes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        recipeId_list = []
        ingredients_list = []
        for row in reader:
            recipeId, *ingredients = row
            recipeId_list.append(recipeId)
            ingredients_list.append(encode(ingredients))
        create_json_file_with_recipes(recipeId_list, ingredients_list)

def create_json_file_with_recipes(recipeId_list: list[int], ingredients_list: list[int]):
    content = {}
    for recipeId, ingredients in zip(recipeId_list, ingredients_list):
        content[recipeId] = ingredients

    with open('recipes.json', 'a') as jsonfile:
        json.dump(content, jsonfile)


if __name__ == "__main__":
    print_rows()