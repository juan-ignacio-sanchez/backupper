from __future__ import unicode_literals

from django.db import models


class Database(models.Model):
    name = models.CharField(max_length=100)


class RemoteDatabase(Database):
    host = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.IntegerField()


class SqliteBackend(Database):
    path = models.CharField(max_length=100)


class MysqlBackend(RemoteDatabase):
    pass


class PsqlBackend(RemoteDatabase):
    pass
