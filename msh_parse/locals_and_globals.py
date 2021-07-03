import json

class Model:
    def __init__(self, json_data: str):
        self.json_data = json_data


def search_class_implementations(class_name):
    globals_variable = list(globals().values())
    models = [i for i in globals_variable if isinstance(i, class_name)]
    print(f'{class_name.__name__}: {models}')


def collection_data_for_interfase():
    search_class_implementations(Model)

if __name__ == "__main__":
    params = {"name": "Olex", "age": "20", "city": "vancuver"}
    json_data = json.dumps(params)
    m = Model(json_data)
    collection_data_for_interfase()
