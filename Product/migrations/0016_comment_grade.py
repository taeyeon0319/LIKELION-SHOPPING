# Generated by Django 3.0.6 on 2020-08-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_auto_20200811_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='grade',
            field=models.IntegerField(null=True, verbose_name='평점'),
        ),
    ]
