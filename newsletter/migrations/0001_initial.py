# Generated by Django 4.0.4 on 2022-07-16 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_newsletteruser', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('creation_date_newsletteruser', models.DateTimeField(default=datetime.datetime(2022, 7, 16, 18, 11, 44, 589666), verbose_name='data de criação')),
                ('activated_newsletteruser', models.BooleanField(default=True, verbose_name='ativado')),
            ],
        ),
    ]