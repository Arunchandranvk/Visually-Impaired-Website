# Generated by Django 4.2.5 on 2024-01-06 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0070_rename_files_answeraudio_fileans_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentansweraudio',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.answeraudio'),
        ),
        migrations.AlterField(
            model_name='studentanswerimage',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.answerimages'),
        ),
    ]
