from event import post_event

def register_new_user(name, password, email):
    user = dict(name=name, password=password, email=email)
    post_event("new_user_created", user)