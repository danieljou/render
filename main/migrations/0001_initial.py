# Generated by Django 4.2.7 on 2023-12-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('tel', models.IntegerField(blank=True, max_length=50, null=True)),
                ('tel2', models.IntegerField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
