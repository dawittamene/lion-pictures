# Generated by Django 4.2.6 on 2023-11-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_delete_gallary_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_h1', models.CharField(max_length=200)),
                ('text_p', models.CharField(max_length=200)),
                ('gallary_post_image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
