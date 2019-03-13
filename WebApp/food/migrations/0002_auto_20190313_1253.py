# Generated by Django 2.1.7 on 2019-03-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='category_long_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='category_short_description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='foodinformation',
            name='food_long_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='foodinformation',
            name='food_short_info',
            field=models.TextField(max_length=250),
        ),
    ]
