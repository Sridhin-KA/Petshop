# Generated by Django 5.0.3 on 2024-06-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsnclaws', '0023_alter_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
