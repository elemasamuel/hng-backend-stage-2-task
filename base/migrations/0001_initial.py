# Generated by Django 4.1.3 on 2022-11-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(max_length=200)),
                ('x', models.IntegerField(max_length=50)),
                ('y', models.IntegerField(max_length=50)),
            ],
        ),
    ]
