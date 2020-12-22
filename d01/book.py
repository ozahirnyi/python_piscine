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

    def get_recipes_by_name(self, name):
        for key, value in self.recipes_list.items():
            if key.split(' ', 1)[0] == name:
                return value
        return "There is nothing to print)"

    def get_recipe_by_types(self, recipe_type):
        for key, value in self.recipes_list.items():
            if key.split(' ', 1)[1] == recipe_type:
                print(value.__str__() + '\n')

    def add_recipe(self, recipe):
        try:
            Recipe.check_data(recipe)
            buf = {recipe.get_name_n_type(): recipe}
            self.recipes_list.update(buf)
            self.last_update = datetime.datetime.now()
        except AttributeError:
            print("Ne naebesh, ne prozhivesh?)")
