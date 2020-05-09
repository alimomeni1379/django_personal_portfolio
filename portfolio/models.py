from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    Description = models.CharField(max_length=250, )
    images = models.ImageField(upload_to='portfolio/iamge')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
