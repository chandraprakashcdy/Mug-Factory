# Generated by Django 2.2.4 on 2019-12-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('JAVA', 'JAVA'), ('.NET', '.NET'), ('PHP', 'PHP'), ('RUBY & RAILS', 'RUBY & RAILS')], max_length=100)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('created_by', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]