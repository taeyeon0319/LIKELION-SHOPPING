# Generated by Django 3.0.6 on 2020-08-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stock',
            field=models.IntegerField(null=True, verbose_name='상품재고'),
        ),
    ]
