# Generated by Django 3.1.7 on 2021-04-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='bodytxt',
            field=models.TextField(),
        ),
    ]