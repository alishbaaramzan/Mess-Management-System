# Generated by Django 5.0.6 on 2024-06-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0002_alter_user_hostel_no_alter_user_mess_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
