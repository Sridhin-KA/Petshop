# Generated by Django 5.0.3 on 2024-06-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsnclaws', '0030_alter_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='owusername',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='payment_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
