# Generated by Django 5.0.3 on 2024-03-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsnclaws', '0003_shop_cat_shop_dog_shop_german_shop_lab_shop_persian_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='dog',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='german',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='persian',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='pit',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='scottis',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='siamese',
        ),
        migrations.AddField(
            model_name='shop',
            name='pet_age',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='pet_breed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='pet_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='pet_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
