from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=100)
    shortdesc = models.TextField(null=True)
    desc = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
