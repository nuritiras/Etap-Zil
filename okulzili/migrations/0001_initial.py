# Generated by Django 4.0.4 on 2022-05-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DuyuruModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık Bilgisi')),
                ('description', models.TextField(max_length=500, verbose_name='İçerik Bilgisi')),
            ],
        ),
    ]
