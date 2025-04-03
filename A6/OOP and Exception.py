class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Item (ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: PHP {self.price:.2f})"


class ItemManagement:
    def __init__(self):
        self.items = {}
        self.next_id = 1  # Automatically incrementing ID

    def create_item(self, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        item = Item(self.next_id, name, description, price)
        self.items[self.next_id] = item
        self.next_id += 1  # Increment ID for the next item
        return item

    def read_item(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        return self.items[item_id]

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        
        item = self.items[item_id]
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            item.price = price
        return item

    def delete_item(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        del self.items[item_id]

    def list_items(self):
        return list(self.items.values())


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    manager = ItemManagement()

    while True:
        print("\n=== Item Management System ===")
        print("        1. Create Item")
        print("        2. Read Item")
        print("        3. Update Item")
        print("        4. Delete Item")
        print("        5. List Items")
        print("        6. Exit")
        print("==============================\n")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = get_float("Enter item price in PHP: ")
            try:
                item = manager.create_item(name, description, price)
                print(f"Item created: {item}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            item_id = int(input("Enter item ID to read: "))
            try:
                item = manager.read_item(item_id)
                print(f"Read item: {item}")
            except KeyError as e:
                print(f"Error: {e}")

        elif choice == '3':
            item_id = int(input("Enter item ID to update: "))
            name = input("Enter new item name (leave blank to keep current): ")
            description = input("Enter new item description (leave blank to keep current): ")
            price_input = input("Enter new item price in PHP (leave blank to keep current): ")
            price = float(price_input) if price_input else None
            try:
                updated_item = manager.update_item(item_id, name or None, description or None, price)
                print(f"Updated item: {updated_item}")
            except KeyError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            item_id = int(input("Enter item ID to delete: "))
            try:
                manager.delete_item(item_id)
                print(f"Deleted item with ID {item_id}.")
            except KeyError as e:
                print(f"Error: {e}")

        elif choice == '5':
            print("All items:")
            items = manager.list_items()
            if items:
                for item in items:
                    print(item)
            else:
                print("No items available.")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()