# Generated by Django 4.2.7 on 2023-12-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_alter_student_first_name_alter_student_last_name'),
        ('home', '0006_notes_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='cat',
            field=models.ForeignKey(default='Very Poor', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.category'),
        ),
    ]
