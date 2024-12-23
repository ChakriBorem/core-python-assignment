class Menu:
    def add(self, menu, item):
        if item not in menu:
            menu.append(item)
            print(f"Updated menu: {menu}")
        else:
            print("Item already exists")

    def remove(self, menu, item):
        if item in menu:
            menu.remove(item)
            print(f"Updated menu: {menu}")
        else:
            print("Item does not exist")

    def check(self, menu, item):
        if item in menu:
            print(f'Availability: "{item} is available"')
        else:
            print(f'Availability: "{item} is not available"')


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
obj = Menu()
add_item = input()
obj.add(initial_menu, add_item)
remove_item = input()
obj.remove(initial_menu, remove_item)
check_item = input()
obj.check(initial_menu, check_item)




