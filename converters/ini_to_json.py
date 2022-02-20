import os
import sys
import json

def tryConvertToNumber(val):
    # to number
    if val.find(".") != -1:
        try:
            val = float(val)
            return val
        except ValueError:
            pass
    else:
        try:
            val = int(val)
        except ValueError:
            pass
    return val


class SmallDictController:
    def __init__(self) -> None:
        self.sectinos = []
        self.data = {}

    def isAlreadyExist(self, name):
        if name in self.sectinos:
            return True
        else:
            return False

    def addNewSection(self, name):
        self.sectinos.append(name)
        self.data[name] = []

    def addedToSection(self, name, value):
        v = self.data.get(name)
        if v is None:
            self.data[name] = [value]
        else:
            v.append(value)
            self.data[name] = v

    def getSmallsDict(self):
        return self.data


class IniToDict:
    window_size_sections = ["Window", "Game"]
    windows_keys = ["ContentResolution", "Size"]

    aspect_sections = ["Game-PC", "Game-IOS", "Game"]

    fonts_keys = ["ColorFont"]

    def __init__(self):
        self.data = {}
        self.tmp_data = []
        self.current_section = None

    def toJson(self):
        return self.data

    def setSection(self, section_name):
        self.current_section = section_name
        self.tmp_data = []
        self.sdc = SmallDictController()

    def addToCurrentSection(self, name, value):
        self.tmp_data.append(name)
        self.tmp_data.append(value)

    def specialParse(self, section, key, value):
        if section in self.window_size_sections and key in self.windows_keys:
            x, y = map(int, value.split(" "))
            return (True, [x, y])

        elif section in self.aspect_sections and key == "AspectRatioViewport":
            a, b, c, d, e, f = map(int, value.split(" "))
            return (True, [a, b, c, d, e, f])

        elif key in self.fonts_keys:
            a = map(int, value.split(" "))
            return (True, [*a])

        return (False, None)

    def packCurrentSection(self):
        if self.current_section == None:
            return

        section_data = {}

        for index, val in enumerate(self.tmp_data):
            # skip values
            if index % 2 != 0:
                continue

            is_special_value, special_value = self.specialParse(self.current_section, val, self.tmp_data[index+1])
            if is_special_value:
                section_data[val] = special_value
                continue

            # have subdict or sublist
            if self.tmp_data.count(val) > 1:
                if not self.sdc.isAlreadyExist(val):
                    self.sdc.addNewSection(val)

                self.sdc.addedToSection(val, tryConvertToNumber(self.tmp_data[index+1]))
            else:
                section_data[val] = tryConvertToNumber(self.tmp_data[index+1])

        self.data[self.current_section] = section_data
        self.data[self.current_section].update(self.sdc.getSmallsDict())


def removeFirstLastSpace(line: str):
    line = line.replace("\n", "")
    if line.startswith(" "):
        line = line[1:]
    if line.endswith(" "):
        line = line[:line.rindex(" ")]
    return line


def isCommit(line):
    return line.startswith(";") or line.startswith("#") or line.startswith("\n")



def parse_ini_file(path) -> IniToDict:
    def isEnd(line):
        return line in ["[END]"]

    new_ini = IniToDict()
    file = open(path)
    file_lines = file.readlines()
    for index, line in enumerate(file_lines):

        if isCommit(line):
            continue

        if index == len(file_lines)-1:
            name, value = map(lambda s: removeFirstLastSpace(s), line.split("="))
            new_ini.addToCurrentSection(name, value)
            new_ini.packCurrentSection()

        elif isEnd(line):
            new_ini.packCurrentSection()

        elif line.startswith("[") and line.endswith("]\n"):
            new_ini.packCurrentSection()
            new_ini.setSection(line[1:line.rindex("]")])

        else:
            name, value = map(lambda s: removeFirstLastSpace(s), line.split("="))
            new_ini.addToCurrentSection(name, value)

    file.close()
    return new_ini.toJson()



def main(path):
    path = os.path.abspath(path)
    # path = os.path.abspath(r"converters\settings.ini")

    if not os.path.isfile(path) or not path.endswith(".ini"):
        raise FileNotFoundError(f"File not found or wrong type: {path}")

    dir_name = os.path.dirname(path)
    file_name, _ = os.path.basename(path).split(".")
    final_file = os.path.join(dir_name, f"{file_name}.json")


    dict_obj = parse_ini_file(path)
    str_obj = str(dict_obj).replace("'", '"')

    json_obj = json.loads(str_obj)

    with open(final_file, "w") as file:
        json.dump(json_obj, file, indent=4)


if __name__ == "__main__":
    print("parse")
    files = sys.argv[1:]
    for file in files:
        main(file)
    # main(".")
