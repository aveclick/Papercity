# Generated by Django 3.2.2 on 2021-06-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='surname',
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
