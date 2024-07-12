class CoffeeShop:
    
    def __init__(self):
        self.menu = {
            "espresso": 2.5,
            "latte": 3.5,
            "cappuccino": 3.0,
            "americano": 2.0,
            "mocha": 3.5
        }
        
        self.inventory = {
            "espresso": 10,
            "latte": 10,
            "cappuccino": 10,
            "americano": 10,
            "mocha": 10
        }
        
        self.sales = 0.0

    def display_menu(self):
        print("\n--- Menu ---")
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")
        print("-------------\n")
    
    def take_order(self):
        self.display_menu()
        order = input("What would you like to order? ").lower()
        if order in self.menu:
            if self.inventory[order] > 0:
                quantity = int(input("How many would you like? "))
                if quantity <= self.inventory[order]:
                    self.process_order(order, quantity)
                else:
                    print(f"Sorry, we only have {self.inventory[order]} {order}(s) left.")
            else:
                print(f"Sorry, we're out of {order}.")
        else:
            print("Sorry, we don't have that item on the menu.")
                    
    def process_order(self, order, quantity):
        cost = self.menu[order] * quantity
        print(f"Your order: {quantity} {order}(s) for ${cost:.2f}")
        confirm = input("Would you like to proceed with the order? (yes/no) ").lower()
          
        if confirm == "yes": 
            self.sales += cost
            self.inventory[order] -= quantity 
            print(f"Thank you! Your order for {quantity} {order}(s) has been placed.")
        else:
            print("Order canceled.")

    def display_sales(self):
        print(f"\nTotal Sales: ${self.sales:.2f}")
        
    def display_inventory(self):
        print("\n--- Inventory ---")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")
        print("------------------\n")

    @staticmethod
    def main():
        shop = CoffeeShop()
        while True:
            print("\nWelcome to the Coffee Shop Management System")
            print("1. Place an order")
            print("2. View sales")
            print("3. View inventory")
            print("4. Exit")
            
            choice = input("Please select an option: ")
            
            if choice == "1":
                shop.take_order()
            elif choice == "2":
                shop.display_sales()
            elif choice == "3":
                shop.display_inventory()
            elif choice == "4":
                print("Thank you for using the Coffee Shop Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    CoffeeShop.main()
