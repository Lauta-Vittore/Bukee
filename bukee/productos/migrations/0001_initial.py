# Generated by Django 4.0.6 on 2022-09-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('precio', models.TextField()),
                ('tipo', models.TextField()),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
    ]