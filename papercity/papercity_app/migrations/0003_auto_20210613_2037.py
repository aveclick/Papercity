# Generated by Django 3.1.7 on 2021-06-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papercity_app', '0002_auto_20210613_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.AddField(
            model_name='genre',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='papercity_app.category'),
        ),
    ]