
class IModel:
    def __str__(self):
        return "This interface for classes"


class StringModel(IModel):
    def __init__(self):
        self.short_string = "This short string"
        super()

    def __str__(self):
        data = f'"short_string": {self.short_string}'
        print(type(data))
        return data


class NotStringModel(IModel):
    def __init__(self):
        self.integer = 123
        super()


    def __str__(self):
        data = f'"integer": {self.integer}'
        return data


class ModelFactory():
    def except_handler(function):
        def run_except_handler(*args):
            try:
                return function(args[0])
                raise AssertionError("Modle not found")
            except AssertionError as _e:
                print(_e)
        return run_except_handler

    @staticmethod
    @except_handler
    def get_model(modeltype: str):
        models = {
            "StringModel": StringModel,
            "NotStringModel": NotStringModel
        }
        return models.get(modeltype)()


