from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #over riding method of AppConfig class
    def ready(self):
        import users.signals
