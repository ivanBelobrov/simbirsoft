# Generated by Django 3.2.9 on 2022-01-22 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='choice', to='polls.question'),
        ),
    ]
