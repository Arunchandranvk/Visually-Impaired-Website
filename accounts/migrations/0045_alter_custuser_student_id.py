# Generated by Django 4.2.5 on 2023-09-26 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_customlogentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cust', to='accounts.student'),
        ),
    ]