import json
import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from services.models import Product  # Import your Product model


def import_data_from_json(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for item in data:
        product = Product(
            productId=item["productId"],
            productPrice=item["productPrice"],
            category=item["category"],
            productTitle=item["productTitle"],
            productDescription=item["productDescription"],
            imageUrl=item["imageUrl"],
            imageUrl1=item["imageUrl1"],
            imageUrl2=item["imageUrl2"],
            imageUrl3=item["imageUrl3"],
        )
        product.save()

    print("Data imported successfully")


if __name__ == "__main__":
    json_file_path = (
        "path_to_your_json_file.json"  # Update with the actual path to your JSON file
    )
    import_data_from_json(json_file_path)
