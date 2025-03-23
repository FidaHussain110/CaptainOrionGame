class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"✅ {item} added to {self.name}'s inventory!")

    def has_item(self, item):
        return item in self.inventory

    def show_inventory(self):
        if self.inventory:
            print(f"🎒 {self.name}'s Inventory: {', '.join(self.inventory)}")
        else:
            print(f"🎒 {self.name}'s Inventory is empty!")