# Generated by Django 3.1.5 on 2021-01-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('writer', models.CharField(blank=True, max_length=50, null=True)),
                ('preview', models.TextField()),
            ],
            options={
                'verbose_name': 'economic_new',
                'verbose_name_plural': 'economic_news',
                'db_table': 'economic_news',
            },
        ),
    ]
