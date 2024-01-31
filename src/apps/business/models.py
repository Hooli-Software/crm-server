from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)


class Order(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=128)
    description = models.TextField()

    date_created = models.DateField(auto_now_add=True)
    date_started = models.DateField()
    date_finished = models.DateField()

    price = models.PositiveIntegerField(default=0, blank=True, null=True)
    hours = models.PositiveIntegerField(default=0, blank=True, null=True)


class Session(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    datetime_start = models.DateTimeField()
    datetime_finish = models.DateTimeField()
