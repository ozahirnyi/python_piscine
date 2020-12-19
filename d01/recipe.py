class Recipe:
    def __init__(self, name, cook_lvl, cook_time, ingredients, description, recipe_type):
        self.name = name
        self.cook_lvl = cook_lvl
        self.cook_time = cook_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.__str__()

    def push_data(self):
        if not isinstance(self.name, str):
            raise AttributeError
        if not isinstance(self.cook_lvl, int) or self.cook_lvl not in range(0, 5):
            raise AttributeError
        if not isinstance(self.cook_time, int) or int(self.cook_time) < 0:
            raise AttributeError
        if not isinstance(self.ingredients, list):
            raise AttributeError
        if not isinstance(self.description, str):
            raise AttributeError
        if not isinstance(self.recipe_type, str) or (self.recipe_type != "starter"
                                                     and self.recipe_type != "lunch"
                                                     and self.recipe_type != "dessert"):
            raise AttributeError

    def __str__(self):
        try:
            self.push_data()
            res = ""
            res = res.join("Name: " + self.name + '\n')
            res = "".join(res + "Cook_lvl: " + str(self.cook_lvl) + '\n')
            res = "".join(res + "Cook_time: " + str(self.cook_time) + '\n')
            res = "".join(res + "Ingredients: " + str(self.ingredients) + '\n')
            res = "".join(res + "Description: " + self.description + '\n')
            res = "".join(res + "Recipe_type: " + self.recipe_type)
            return res
        except AttributeError:
            print("• name (str)\n"
                  "• cooking_lvl (int) : range 1 to 5\n"
                  "• cooking_time (int) : in minutes (no negative numbers)\n"
                  "• ingredients (list) : list of all ingredients each represented by a string\n"
                  "• description (str) : description of the recipe\n"
                  "• recipe_type (str) : can be 'starter', 'lunch' or 'dessert'.)")
