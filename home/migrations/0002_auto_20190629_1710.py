# Generated by Django 2.2.2 on 2019-06-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=100, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='メッセージ'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名前'),
        ),
    ]
