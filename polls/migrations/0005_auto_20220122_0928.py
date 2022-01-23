# Generated by Django 3.2.9 on 2022-01-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20220122_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='polls.userprofile'),
        ),
    ]
