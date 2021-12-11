from user import register_new_user
from email_handler import setup_email_event_handlers
from database_handler import setup_database_event_handlers

setup_email_event_handlers()
setup_database_event_handlers()

register_new_user('Jakub', 'secret', 'name@domain.edu')