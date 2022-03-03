import json

def load_data():
    with open('data/data.json', encoding='utf8') as f:
        data = json.load(f)
    return data


def define_page(id):
    data = load_data()
    for article in data:
        if id == article["name"]:
            return article