# Generated by Django 3.2.9 on 2021-11-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_id', models.CharField(max_length=50)),
                ('acc_email', models.EmailField(max_length=254)),
                ('acc_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
