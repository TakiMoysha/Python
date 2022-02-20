import os
import sys
import json


class GlobalVars:
    preargs = "run"
    prevars = "set"

    is_json_body = False


class JsonObject:
    vars = "vars"

    def __init__(self, name) -> None:
        self.name = name
        self.data = {}

    def write_var(self, var_name, var_value):
        if self.data.get(self.vars) is None:
            self.data[self.vars] = {}

        self.data[self.vars].update({var_name: var_value})

    def write_arg(self, arg_name, arg_value):
        arg_name = arg_name.replace("-", "")
        self.data[arg_name] = arg_value

    def save(self):
        self.name = self.name.replace(".bat", ".json")
        with open(f"./{self.name}", "w") as file:
            json.dump(self.data, file, indent=2)


def correct_type(arg_value):
    arg_value = arg_value.replace('\n', '').replace('"', '')

    if arg_value == "enable":
        return True
    elif arg_value == "disable":
        return False
    try:
        return int(arg_value)
    except ValueError:
        return arg_value.replace("\\\\", "\\")


def individual_rules(arg_name: str, arg_value: str):
    if arg_name.endswith("path_app_ini"):
        arg_name = arg_name.replace("ini", "json")
        arg_value = arg_value.replace("ini", "json")

    return (arg_name, arg_value)


def parse_line(js_obj: JsonObject, line: str):
    if line.startswith(GlobalVars.preargs):
        GlobalVars.is_json_body = True

    elif line.startswith(GlobalVars.prevars):
        var = line[line.index('"')+1:line.rindex('"')]
        var_name, var_value = var.split("=")
        js_obj.write_var(var_name, var_value)

    elif GlobalVars.is_json_body and line == "\n":
        GlobalVars.is_json_body = False

    elif GlobalVars.is_json_body:
        arg_name, arg_value, *_ = line.split(" ")
        arg_name, arg_value = individual_rules(arg_name, arg_value)
        arg_value = correct_type(arg_value)
        js_obj.write_arg(arg_name, arg_value)


def main(*args):
    path = args[0]

    if not os.path.isfile(path) or not path.endswith(".bat"):
        raise FileNotFoundError(f"File not found or wrong type: {path}")

    new_json = JsonObject(os.path.basename(path))
    with open(path, 'r') as file:
        for line in file:
            parse_line(new_json, line)

    new_json.save()


if __name__ == "__main__":
    main(*sys.argv[1:])