from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):  # menages the signals during creating user
        import accounts.signals