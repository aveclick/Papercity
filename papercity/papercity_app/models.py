from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_list", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Author(models.Model):
    """Авторы"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Genre(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Books(models.Model):
    """Книги"""
    id = models.IntegerField
    title = models.CharField('Название', max_length=50)
    author = models.ManyToManyField(Author, verbose_name='автор')
    genre = models.ManyToManyField(Genre, verbose_name='жанр')
    description = models.TextField(max_length=3000)
    price = models.PositiveIntegerField('Стоимость', default=0)
    count = models.PositiveIntegerField('В наличии', default=1)
    photo = models.ImageField(upload_to="books/%Y/%m/%d/")
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Books, verbose_name='книга', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    count = models.IntegerField("Количество")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

