class Recipe:
    def __init__(self, name, cook_lvl, cook_time, ingredients, description, recipe_type):
        self.name = name
        self.cook_lvl = cook_lvl
        self.cook_time = cook_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def push_data(self):
        if not isinstance(str, self.name):
            raise AttributeError
        if not isinstance(int, self.cook_lvl) or self.cook_lvl not in range(0, 5):
            raise AttributeError
        if not isinstance(int, self.cook_time) or int(self.cook_time) < 0:
            raise AttributeError
        if not isinstance(list, self.ingredients):
            raise AttributeError
        if not isinstance(str, self.description):
            raise AttributeError
        if not isinstance(str, self.recipe_type) or self.recipe_type != "starter":
            raise AttributeError

    def __str__(self):
        return self
