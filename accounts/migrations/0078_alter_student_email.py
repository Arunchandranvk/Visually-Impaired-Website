# Generated by Django 5.0.3 on 2024-04-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0077_categorys_alter_scoremodel_cat_alter_suggestion_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
