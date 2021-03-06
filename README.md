# django_papercity
Книжный магазин на Django

# Введение
#### Описание: Книжный магазин с функциями поиска, регистрации, авторизации и каталогами.

# Структура проекта

## Главная страница + каталог
На главной странице представлен слайдер с последними акциями магазина и несколько блоков с подборками книг. В верхнем меню можно перейти в каталог, где представлены различные категории книг. В меню, расположенном с левой стороны, также представлены все категории.

![1](/screenshots/1.PNG)

![2](/screenshots/2.PNG)

## Страница товара
На странице товара представлен товар (книга) с указанием автора, описанием и возможностью добавления в корзину, которая доступна после авторизации.

![3](/screenshots/3.PNG)

## Поиск
Поиск по сайту выполнен с применением баз данных. 

![4](/screenshots/4.PNG)

## Отзывы
На сайте есть возвожность добавления отзыва к опредленному товару. Необходимо указать имя и текст отзыва. Эта функция доступна без авторизации.

![5](/screenshots/5.png)

![6](/screenshots/6.png)

## Профиль
Просмотр профиля доступен пользователям после авторизации/регистрации. Также данные можно редактировать.

![7](/screenshots/7.png)

![8](/screenshots/8.png)

# Первый запуск
```
git clone https://github.com/aveclick/django_papercity.git
cd papercity
pip install django
pip install Pillow
pip install django-crispy-forms
python manage.py runserver
```

22.06.2021
