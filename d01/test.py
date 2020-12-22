from recipe import Recipe
from book import Book

rec = Recipe("grecha1", 1, 15, ["kz", "25 kartoshek", "12 manda"],
             "nu eta ochen vkusna, pravda", "starter")
rec1 = Recipe("grecha2", 2, 15, ["kz", "25 kartoshek", "12 manda"],
             "nu eta ochen vkusna, pravda", "lunch")
rec2 = Recipe("grecha3", 3, 15, ["kz", "25 kartoshek", "12 manda"],
             "nu eta ochen vkusna, pravda", "dessert")
rec3 = Recipe("grecha4", 4, 15, ["kz", "25 kartoshek", "12 manda"],
             "nu eta ochen vkusna, pravda", "starter")
book = Book()
book.add_recipe(rec)
book.add_recipe(rec1)
book.add_recipe(rec2)
book.add_recipe(rec3)
print(book.creation_date.strftime("%c"))
print(book.last_update.strftime("%c"))
print(book.get_recipe_by_types("starter"))
# print(book.get_recipes_by_name("grecha4"))

