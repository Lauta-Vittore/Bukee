# Generated by Django 4.0.6 on 2022-09-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webBukee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tallas',
            fields=[
                ('talla', models.TextField(blank=True, db_column='Talla', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Tallas',
                'managed': False,
            },
        ),
    ]
