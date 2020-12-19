import datetime
from recipe import Recipe


class Book:
    name = ""
    last_update = datetime.MAXYEAR
    creation_date = datetime.MINYEAR
    recipes_list = {}

    def __init__(self):
        print("Book created!")
        self.creation_date = datetime.datetime.now()

    # def get_recipes_by_types(self, recipe_type):

    def get_recipe_by_name(self, name):
        return self.recipes_list.get(name)

    def add_recipe(self, recipe):
        try:
            Recipe.check_data(recipe)
            self.recipes_list.update({recipe.recipe_type: recipe})
            self.last_update = datetime.datetime.now()
        except AttributeError:
            print("Ne naebesh, ne prozhivesh?)")