from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='Parent category', related_name='children', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    @property
    def path(self):
        parents = ''
        current = self

        while True:
            if current.parent:
                parents = current.parent.name + ' / ' + parents
                current = current.parent
            else:
                break

        return parents+self.name



class Unit(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Category', related_name='units', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)