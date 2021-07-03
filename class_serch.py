
import msh_parse.runner
import msh_parse.msh_data as data

class FirstModel(data.Model):
    def __init__(self, name: str):
        self.name = name
        super()

    def __str__(self):
        return self.name


if __name__ == "__main__":
    pass
    # fm = FirstModel("Name_first")
