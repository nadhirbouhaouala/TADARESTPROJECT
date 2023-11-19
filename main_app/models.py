from django.db import models

# Create your models here.

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True , null = True)
    file = models.FileField()
    comment = models.TextField(default = "")
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Task._meta.fields[1:]]
    def __str__(self):#toString
        return self.file
