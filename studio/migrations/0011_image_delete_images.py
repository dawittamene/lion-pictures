# Generated by Django 4.2.6 on 2023-11-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0010_gallary_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
