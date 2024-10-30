from django.db import models # type: ignore

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
