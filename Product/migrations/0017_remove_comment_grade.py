# Generated by Django 3.0.6 on 2020-08-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_comment_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='grade',
        ),
    ]