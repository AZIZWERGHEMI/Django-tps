# Generated by Django 5.0.2 on 2024-05-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0010_alter_commande_totalcde'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produitc',
            old_name='Duree_garantie',
            new_name='duree_garantie',
        ),
        migrations.RenameField(
            model_name='produitnc',
            old_name='Duree_garantie',
            new_name='duree_garantie',
        ),
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.FloatField(editable=False),
        ),
    ]