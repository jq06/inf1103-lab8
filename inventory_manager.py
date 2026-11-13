from file_handler import load_inventory, save_inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


def get_float_input(message):
    while True:
        try:
            value = float(input(message).strip())

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(message):
    while True:
        try:
            value = int(input(message).strip())

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("INVENTORY MANAGEMENT SYSTEM")

    inventory = load_inventory()

    while True:
        print("\nMENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            print("\nAdd New Product")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Select product type: ").strip()

            if product_type != "1" and product_type != "2":
                print("Invalid product type.")
                continue

            prod_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()

            if prod_id == "" or name == "":
                print("Product ID and name cannot be empty.")
                continue

            price = get_float_input("Price: $")
            stock = get_int_input("Stock Quantity: ")

            if product_type == "1":
                weight = get_float_input("Weight (kg): ")

                product = PhysicalProduct(
                    prod_id, name, price, stock, weight
                )

            else:
                download_size = get_float_input("Download Size (MB): ")

                product = DigitalProduct(
                    prod_id, name, price, stock, download_size
                )

            inventory.add_product(product)
            print("Product added successfully!")

        elif choice == "3":
            print("\nUpdate Stock")

            prod_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(prod_id)

            if product is None:
                print("Product not found.")
                continue

            print("\nProduct Found:")
            print(f"Name: {product.name}")
            print(f"Current Stock: {product.stock}")

            new_stock = get_int_input("New Stock Quantity: ")

            product.update_stock(new_stock)

            print("Stock updated successfully!")

        elif choice == "4":
            print("\nSearch Product")

            prod_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(prod_id)

            if product is None:
                print("\nProduct not found.")

            else:
                print("\nProduct Found")
                product.display_information()

                print(f"Fulfilment: {product.get_fulfilment_info()}")

                if isinstance(product, PhysicalProduct):
                    print(
                        f"Shipping Cost: "
                        f"${product.calculate_shipping_cost():.2f}"
                    )

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")

            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()