class Email:
    @staticmethod
    def send_email(email, subject, message):
        print("===================")
        print(f'From {email}\nSubject: {subject}\n{message}')
        print("===================")


class Database:
    users = []
    @classmethod
    def register_new_user(cls, user):
        cls.users.append(user)
        print("===================")
        print(f'New user: {user}\nUsers: {cls.users}')
        print("===================")