from app_tools import Email
from event import subscribe

def handle_user_registered_event(user):
    Email.send_email(user['email'], "Welcome!", "Some welcome message")

def setup_email_event_handlers():
    subscribe("new_user_created", handle_user_registered_event)