# Generated by Django 5.0.2 on 2024-05-10 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_produit_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='total',
            new_name='totalCde',
        ),
    ]