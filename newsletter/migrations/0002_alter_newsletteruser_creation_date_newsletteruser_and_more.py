# Generated by Django 4.0.4 on 2022-07-16 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='creation_date_newsletteruser',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 16, 18, 17, 10, 891373), verbose_name='data de criação'),
        ),
        migrations.AlterField(
            model_name='newsletteruser',
            name='email_newsletteruser',
            field=models.EmailField(max_length=254, unique=True, verbose_name='e-mail'),
        ),
    ]