from django.db import models
import datetime
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    content = models.TextField(default='Content')
    slug = models.SlugField(default='slug')
    published = datetime.date.today()
    active  = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
