cook_book = {}
with open("first recept.txt") as new_cookbook:
  line = new_cookbook.readline()
  while line != '':
    recept_name = line.strip()
    ingr_count = int(new_cookbook.readline())
    ingr = {}
    new_ingr = []
    for result in range(ingr_count):
      tmp = new_cookbook.readline().split('|')
      ingredient_name = tmp[0].strip()
      quantity = tmp[1].strip()
      measure = tmp[2].strip()
      ingredient_name = {'ingredient_name': ingredient_name,'quantity': quantity,'measure': measure}
      new_ingr.append(ingredient_name)
    ingr[recept_name] = new_ingr
    cook_book.update(ingr)
    new_cookbook.readline()
    line = new_cookbook.readline()

print(cook_book)
