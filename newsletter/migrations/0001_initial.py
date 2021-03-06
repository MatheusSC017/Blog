# Generated by Django 4.0.4 on 2022-07-19 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_newslettermessage', models.CharField(max_length=998, verbose_name='título')),
                ('message_newslettermessage', models.TextField(verbose_name='mensagem')),
                ('creation_date_newslettermessage', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criação')),
                ('edition_date_newslettermessage', models.DateTimeField(default=django.utils.timezone.now, verbose_name='última edição')),
                ('published_newslettermessage', models.BooleanField(default=False, verbose_name='publicado')),
            ],
            options={
                'verbose_name': 'mensagem',
                'verbose_name_plural': 'mensagens',
            },
        ),
        migrations.CreateModel(
            name='NewsLetterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_newsletteruser', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('creation_date_newsletteruser', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criação')),
                ('activated_date_newsletteruser', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de ativação')),
                ('activated_newsletteruser', models.BooleanField(default=True, verbose_name='ativado')),
            ],
            options={
                'verbose_name': 'usuário',
            },
        ),
    ]
