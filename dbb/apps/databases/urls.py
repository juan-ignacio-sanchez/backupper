from django.conf.urls import url
from .views import databases, make_backup, databases_list


urlpatterns = [
    url(r'^databases/$', databases_list, name="databases_list"),
    url(r'^databases/new$', databases, name="databases_new"),
    url(r'^databases/backup/$', make_backup, name="databases_backup")
]

