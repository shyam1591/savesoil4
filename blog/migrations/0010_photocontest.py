# Generated by Django 4.0.5 on 2022-08-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_comm_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photocontest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted'],
            },
        ),
    ]