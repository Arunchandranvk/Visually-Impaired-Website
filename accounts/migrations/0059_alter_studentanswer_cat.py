# Generated by Django 4.2.7 on 2023-12-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0058_rename_category_studentanswer_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='cat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
