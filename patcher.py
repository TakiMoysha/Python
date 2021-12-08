import os
import sys
import json
import shutil
import zipfile

from functools import reduce
from datetime import datetime

NEEDED_BACKUP = False

class SystemPath(str):
    def __init__(self, path):
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise FileNotFoundError("I can't find the path: {}".format(path))

        self.path = path

    def __str__(self):
        return str(self.path)

class Task:
    def __init__(self):
        self.for_backup = []
        self.for_remove = []

    def run(self):
        raise NotImplementedError("Function not implement")

    def finalize(self):
        raise NotImplementedError("Function not implement")


class RewriteJson(Task):
    def __init__(self, goal_path, patch_path):
        super().__init__()
        self.goal_path = goal_path
        self.patch_path = patch_path

    def run(self):
        self.for_backup.append(self.goal_path)
        self.goal_content = js_load(self.goal_path)
        patch_content = js_load(self.patch_path)

        delete_unnecessary_sections(self.goal_content)

        self.goal_content.update(patch_content)

        if self.goal_path.endswith("packages.json"):
            localizations = self.goal_content["GAME_PACKAGES"].get("LanguagePack")
            project_folder_path = os.path.dirname(self.goal_path)
            localization_path = SystemPath("{}/Localizations/".format(project_folder_path))
            self.for_removed = self.for_removed + search_useless_folders(localization_path, localizations)
            [self.for_backup.append(abs_path) for abs_path in self.for_removed]

    def finalize(self):
        js_save(self.goal_path, self.goal_content)
        delete_by_paths(self.for_remove)


class RewriteLogo(Task):
    def __init__(self, goal_path, patch_path):
        super().__init__()
        self.goal_path = goal_path
        self.patch_path = patch_path

    def run(self):
        self.for_backup.append(self.goal_path)

    def finalize(self):
        rewrite_logo(self.patch_path, self.goal_path)


class RemoveFile(Task):
    def __init__(self, goal_path):
        super().__init__()
        self.goal_path = goal_path

    def run(self):
        self.for_backup.append(self.goal_path)
        self.for_remove.append(self.goal_path)

    def finalize(self):
        delete_by_paths(self.for_remove)


class Backup:
    time_format = r"%d_%m_%y-%H_%M"
    backup_folder = os.path.abspath(".")
    paths_for_backup = list()

    @classmethod
    def init(cls):
        pass

    @classmethod
    def add_to_backup(cls, path):
        cls.paths_for_backup.append(path)

    @classmethod
    def create_backup(cls):
        backup_name = "{}.zip".format(datetime.strftime(datetime.now(), cls.time_format))
        path = os.path.join(cls.backup_folder, backup_name)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zfile:
            for path in cls.paths_for_backup:
                zfile.write(str(path), arcname="{}".format(os.path.basename(str(path))))


def parse_args(*args):
    tasks = []
    for arg in args:
        abs_origin_file, abs_patch = arg.split("=")

        if abs_origin_file.endswith("json"):
            rewrite_json = RewriteJson(SystemPath(abs_origin_file), SystemPath(abs_patch))
            tasks.append(rewrite_json)

        elif abs_origin_file == 'remove':
            remove_file = RemoveFile(SystemPath(abs_patch))
            tasks.append(remove_file)

        elif abs_origin_file.endswith("jpeg") or abs_origin_file.endswith("jpg") or abs_origin_file.endswith("png"):
            rewrite_logo = RewriteLogo(SystemPath(abs_origin_file), SystemPath(abs_patch))
            tasks.append(rewrite_logo)

        else:
            raise BaseException("I don't know file format: {}".format(abs_origin_file))

        print("Goal: {}\nPatch: {}".format(abs_origin_file, abs_patch))

    return tasks


def js_load(path):
    with open(path) as f:
        content = json.load(f)
    return content


def js_save(path, content):
    with open(path, "w") as f:
        json.dump(content, f, indent=4)


def delete_unnecessary_sections(content):
    gp = "GAME_PACKAGES"
    section_gp = content.get(gp)
    if section_gp is not None:
        sections_must_exist = reduce(lambda x,y: x + y, section_gp.values())
        sections_must_exist.append(gp)
        keys = list(content.keys())
        for key in keys:
            if key not in sections_must_exist:
                del content[key]


def rewrite_logo(new, old):
    name, file_format = os.path.basename(old).split(".")
    _, new_file_format = os.path.basename(new).split(".")
    final_name = ".".join([name, new_file_format])
    final_path = os.path.abspath("{}/{}".format(os.path.dirname(old), final_name))
    shutil.copyfile(new, final_path)


def search_useless_folders(path, localizations_names):
    useless_folders = []
    dirs = os.listdir(str(path))
    for local_dir in dirs:
        if local_dir not in localizations_names:
            useless_folders.append(os.path.join(str(path), local_dir))

    return useless_folders


def delete_by_paths(paths):
    for path in paths:
        path = str(path)
        print("Delete: {}".format(path))
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)


def main(tasks):
    print("Init...")
    for task in tasks:
        task.run()
        [Backup.add_to_backup(path) for path in task.for_backup]

    if NEEDED_BACKUP:
        Backup.create_backup()

    print("Finalize...")
    [task.finalize() for task in tasks]


if __name__ == "__main__":
    Backup.init()

    args = sys.argv[1:]

    # args = (
    #     r'.\job_scripts\patcher\goal_folder\Configs.json=.\job_scripts\patcher\patches\ua.json',
    #     r'.\job_scripts\patcher\goal_folder\logo_b.jpeg=.\job_scripts\patcher\patches\logo_patch.jpeg',
    #     r'remove=.\job_scripts\patcher\patches\logo_patch1.jpeg',
    # )

    task = parse_args(*args)
    main(task)
