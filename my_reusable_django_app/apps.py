from django.apps import AppConfig


class MyReusableDjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_reusable_django_app'
