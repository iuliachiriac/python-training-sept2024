# 3. Create class Dish - instance attributes: id (int), name (str), price (int)

class Dish:
    def __init__(self, id_, name, price):
        self.id = id_
        self.name = name
        self.price = price

    def __eq__(self, other):
        return (self.id == other.id and
                self.name == other.name and
                self.price == other.price)

    def __repr__(self):
        return f"{self.__class__.__name__} object (id={self.id} "\
               f"name={self.name} price={self.price})"


# 4. Create class Menu - instance attributes: dishes (list of Dish objects).
# Implement appropriate methods so that Menu objects support the following
# operations:
#  d = Dish(0, 'Lasagna', 20)
#  m = Menu()
#  m += d  # dish appended to m.dishes
#  m[0]  # implement getitem on Menu
#  d in m  # implement membership test operators
#  len(m)  # return length of m.dishes

class Menu:
    def __init__(self, dishes=None):
        self.dishes = dishes or []

    def __iadd__(self, dish):
        self.dishes.append(dish)
        return self

    def __getitem__(self, idx):
        for dish in self.dishes:
            if idx == dish.id:
                return dish

    def __contains__(self, dish):
        return dish in self.dishes

    def __len__(self):
        return len(self.dishes)


dish1 = Dish(1, 'Lasagna', 30)
dish2 = Dish(2, 'Pizza', 35)
dish3 = Dish(3, 'Pasta', 32)

menu = Menu()
menu += dish1
menu += dish2
print("First item on the menu:", menu[1])
print(dish2, "is on the menu:", dish2 in menu)
print(dish3, "is on the menu:", dish3 in menu)
print("Number of items in the menu:", len(menu))


# Have 2 dishes created with same values d1 and d2. Add d1 to the menu instance m. Test membership of d2 in m. Does it find d2 in menu? Why?

d1 = Dish(4, 'Salad', 30)
d2 = Dish(4, 'Salad', 30)
menu += d1
print("d2 in menu", d2 in menu)

# Modify Dish to test for equality by looking at dish_id, name, price being the same, so that dishes above would make this true d1 == d2. Test d2 in m again.
# Modify the getitem dunder to get the dish with the dish_id equal witht the argument given. Raise KeyError if not found