# Generated by Django 2.2.4 on 2019-12-21 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_factory'),
    ]

    operations = [
        migrations.AddField(
            model_name='mug',
            name='factory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Factory'),
            preserve_default=False,
        ),
    ]
