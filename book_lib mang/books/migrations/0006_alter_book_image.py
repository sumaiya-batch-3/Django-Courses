# Generated by Django 4.2.4 on 2024-03-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='books/media/uploads'),
        ),
    ]
