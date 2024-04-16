from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, default="home")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, default="/")
    named_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
