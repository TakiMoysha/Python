import datetime

# personal info
full_name = "Mikhail Popov"

# residence
contry = "Russian Federation"
city = "Voronezh"

# communicate
telephone = "+7(904)212-52-68"
email = "mpwema782@gmail.com"

# links
linkedin = "www.linkedin.com/in/takimoysha"
github = "www.github.com/TakiMoysha"

# -----------------------------
summary = "Apply for Python Junior Developer\nNow participate in the development of a game server as a TypeScript developer. Ready to move to another country"

# -----------------------------
class Project:
    __slots__ = ('project_name', 'date', 'desc')

    def __init__(self, name, date, desc) -> None:
        self.project_name = name
        self.date = date
        self.desc = desc

game_launcher_desc = 'Python3 + PySide6 (Qt) application\nAllows you to select the authorization server and game server. Connect to the server, download required files, start the game'
home_server_des = 'Django\nUsed as file storage, it provides a personal account into which you can record information and remotely print files to a printer'
resume_builder_desc = 'Django, reportlab\nCreate resume from PDF'
projects = [
    Project("Game Luncher", datetime.date(2021, 6, 1), game_launcher_desc),
    Project("Home server", datetime.date(2021, 4, 1), game_launcher_desc),
    Project("Resume builder", datetime.date(2020, 12, 5), game_launcher_desc),
]

# -----------------------------
class Education:
    __slots__ = ('name', 'university', 'location', 'year')

    def __init__(self, name, university, location, year) -> None:
        self.name = name
        self.university = university
        self.location = location
        self.year = year

Education("Bachelor of Informatics and computer engineering", "Voronezh State University",
    "Russia, Voronezh", "2021"
)
# -----------------------------
skills = {
    "Languages": "Python, JavaScript/TypeScript, Dart, Java, HTML, CSS",
    "OS": "Windows, Linux",
    "Database": "PostgreSQL, MongoDB, MySQL",
    "Other": "Zabbix, Git, NGINX, Apache, Docker",
    "Other": "Zabbix, Git, NGINX, Apache, Docker",
    "English": "A2/Pre-Intermediate",
    "Russian": "native"
}