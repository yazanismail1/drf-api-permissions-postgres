# Generated by Django 4.1.4 on 2022-12-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=models.DateField(help_text='Enter the DOB in this format YYY-MM-DD'),
        ),
    ]
