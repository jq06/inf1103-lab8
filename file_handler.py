import json
import os

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


def load_inventory():
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)

            for item in data:

                if item["type"] == "physical":
                    product = PhysicalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"]
                    )

                elif item["type"] == "digital":
                    product = DigitalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )

                else:
                    print("Unknown product type. Product skipped.")
                    continue

                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Error loading inventory.json, starting with empty inventory.")
            inventory = Inventory()

    else:
        print("inventory.json not found. Starting with empty inventory.")

    return inventory


def save_inventory(inventory):
    print("\nSaving inventory...")

    data = []

    for product in inventory.get_products():

        if isinstance(product, PhysicalProduct):

            data.append({
                "type": "physical",
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "weight": product.weight
            })

        elif isinstance(product, DigitalProduct):

            data.append({
                "type": "digital",
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "download_size": product.download_size
            })

    with open("inventory.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Inventory saved successfully to inventory.json.")