from django.db import models

# Create your models here.


class Tag(models.Model):
    """
    Модель для тегов новостей.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Модель для категорий новостей.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Модель для статей.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title
