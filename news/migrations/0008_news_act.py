# Generated by Django 3.2.3 on 2021-06-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_ocatid'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
