# Generated by Django 2.0 on 2018-01-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='postcode',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='receiver',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
    ]