# Generated by Django 5.0.3 on 2024-06-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsnclaws', '0032_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
