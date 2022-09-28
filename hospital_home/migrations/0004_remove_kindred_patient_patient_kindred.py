# Generated by Django 4.1.1 on 2022-09-28 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_home', '0003_user_remove_assistant_address_remove_assistant_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kindred',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='kindred',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_home.kindred'),
        ),
    ]
