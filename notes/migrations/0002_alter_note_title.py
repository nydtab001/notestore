# Generated by Django 3.2.17 on 2023-06-21 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]