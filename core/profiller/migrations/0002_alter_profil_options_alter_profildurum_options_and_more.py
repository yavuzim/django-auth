# Generated by Django 5.0.3 on 2024-03-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Profiller'},
        ),
        migrations.AlterModelOptions(
            name='profildurum',
            options={'verbose_name_plural': 'Profil Mesajları'},
        ),
        migrations.AlterField(
            model_name='profil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profil_fotolari/%Y/%m/'),
        ),
    ]
