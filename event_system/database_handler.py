from app_tools import Database
from event import subscribe

def handle_user_registered_event(user):
    Database.register_new_user(user)


def setup_database_event_handlers():
    subscribe('new_user_created', handle_user_registered_event)