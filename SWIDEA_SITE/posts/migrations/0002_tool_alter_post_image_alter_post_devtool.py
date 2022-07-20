# Generated by Django 4.0.6 on 2022-07-20 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='툴이름')),
                ('type', models.CharField(max_length=20, verbose_name='툴종류')),
                ('content', models.TextField(verbose_name='툴설명')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/%Y%m%d', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='post',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tool', to='posts.tool'),
        ),
    ]
