# Generated by Django 3.0.5 on 2022-12-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(2, 2), (3, 3)]),
        ),
    ]
