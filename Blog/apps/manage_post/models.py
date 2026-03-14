from django.db import models

# We bring on our own "User Entity" instead of default user_auth from Django
    # settings.py --> AUTH_USER_MODEL = 'user.User'
from django.contrib.auth import get_user_model

User = get_user_model()


# New Model - Category

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    #equivalent to "@Entity, @Table... etc"
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# New Model - Article

class Article(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


# New Model - Article

class Rating(models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
            #equivalent:
            #SELECT username
            #FROM user
            #WHERE id = user_id
        return self.user_id.username

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'