from django.apps import AppConfig


class BuyerProfileConfig(AppConfig):
    name = 'buyer_profile'

    def ready(self):
        import buyer_profile.signals
        print("ready")
