# Generated by Django 3.1.4 on 2022-05-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20220501_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='photo',
            field=models.ImageField(default='https://th.bing.com/th/id/OIP.kuzAfGlfkzL7e0uRhy0wVAAAAA?pid=ImgDet&rs=1', upload_to='pics'),
            preserve_default=False,
        ),
    ]
