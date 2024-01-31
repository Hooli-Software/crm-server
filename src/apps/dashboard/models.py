from django.db import models


class HabitCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        path = ''
        current_node = self.parent

        while True:
            if current_node:
                path += current_node.title + ' / '
                current_node = current_node.parent
            else:
                break

        return path + self.title


class HabitUnit(models.Model):
    value = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    category= models.ForeignKey(HabitCategory, on_delete=models.SET_NULL, null=True)


class PeriodCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        path = ''
        current_node = self.parent

        while True:
            if current_node:
                path += current_node.title + ' / '
                current_node = current_node.parent
            else:
                break

        return path + self.title


class PeriodUnit(models.Model):
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(PeriodCategory, on_delete=models.SET_NULL, null=True)


class PeriodMessage(models.Model):
    unit = models.ForeignKey(PeriodUnit, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)