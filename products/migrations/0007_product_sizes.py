# Generated by Django 3.2.25 on 2024-06-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20240611_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.JSONField(blank=True, null=True),
        ),
    ]