# Generated by Django 4.1.4 on 2022-12-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0002_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(verbose_name='about')),
                ('education', models.TextField(verbose_name='education')),
                ('intrests', models.TextField(verbose_name='intrests')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=120, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='title'),
        ),
    ]
