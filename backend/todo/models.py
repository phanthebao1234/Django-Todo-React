from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    complete = models.BooleanField(default=False)

    def _str_(self):
        return self.title