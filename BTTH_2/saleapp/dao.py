import json

from saleapp import app


def load_products():
    with open(f'{app.root_path}/data/products.json', encoding='utf-8') as f:
        return json.load(f)