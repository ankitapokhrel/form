# Generated by Django 4.1.3 on 2022-11-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Form',
            },
        ),
        migrations.DeleteModel(
            name='Sorm',
        ),
    ]
