import json

class Model:
    def __init__(self, as_json: dict):
        self.json_data = json.dumps(as_json)


def search_class_implementations(class_name):
    globals_variable = list(globals().values())
    models = [i for i in globals_variable if isinstance(i, class_name)]
    print(f'{class_name.__name__}: {models}')


def data_collection_for_interface():
    search_class_implementations(Model)


if __name__ == "__main__":
    params = {"name": "Olex", "age": "20", "city": "vancuver"}
    m = Model(params)
    data_collection_for_interface()
