# Generated by Django 4.1 on 2022-09-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mairie', '0003_une_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('fichier', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
