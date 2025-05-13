from django.urls import path

from catalog.views import contacts_view, home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("contacts/", contacts_view, name="contacts"),
]
