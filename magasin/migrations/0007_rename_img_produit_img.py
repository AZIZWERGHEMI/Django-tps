# Generated by Django 5.0.2 on 2024-03-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_produitc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='Img',
            new_name='img',
        ),
    ]
