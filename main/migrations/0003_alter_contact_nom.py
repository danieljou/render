# Generated by Django 4.2.7 on 2023-12-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_contact_tel_alter_contact_tel2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]