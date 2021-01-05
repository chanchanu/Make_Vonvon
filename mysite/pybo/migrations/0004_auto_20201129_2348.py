# Generated by Django 3.0.3 on 2020-11-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_auto_20201129_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128)),
                ('content1', models.IntegerField()),
                ('content2', models.IntegerField()),
                ('content3', models.IntegerField()),
                ('content4', models.IntegerField()),
                ('content5', models.IntegerField()),
                ('content6', models.IntegerField()),
                ('content7', models.IntegerField()),
                ('content8', models.IntegerField()),
                ('content9', models.IntegerField()),
                ('content10', models.IntegerField()),
                ('tit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Quiz')),
            ],
        ),
        migrations.DeleteModel(
            name='S',
        ),
    ]
