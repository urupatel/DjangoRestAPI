# Generated by Django 4.0.3 on 2022-04-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
