import json
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trendy.settings")
django.setup()

from services.models import Product


def import_data_from_json(json_file_path):
    with open(
        "/home/aryangupta/Personal_Space/Trendy_Backend/productDetailData.json", "r"
    ) as file:
        data = json.load(file)

    for item in data:
        product = Product(
            id=item["id"],
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
        "/home/aryangupta/Personal_Space/Trendy_Backend/productDetailData.json"
    )
    import_data_from_json(json_file_path)
