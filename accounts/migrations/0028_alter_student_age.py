# Generated by Django 4.2.5 on 2023-09-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_question_student_category_student_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]