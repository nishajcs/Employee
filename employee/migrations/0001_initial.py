# Generated by Django 5.0.4 on 2024-05-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('job_title', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='images/default_image.jpg', upload_to='images')),
            ],
        ),
    ]
