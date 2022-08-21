# Generated by Django 3.2.6 on 2022-08-14 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220814_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=50, verbose_name='дата')),
                ('description', models.TextField(blank=True, verbose_name='празник(необезательно)')),
                ('time', models.CharField(blank=True, max_length=200, verbose_name='время службы')),
            ],
            options={
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.AlterModelOptions(
            name='imgnews',
            options={'verbose_name_plural': 'Фото к новостям'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='imgnews',
            name='category_news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.news', verbose_name='новость'),
        ),
        migrations.AlterField(
            model_name='imgnews',
            name='image',
            field=models.ImageField(blank=True, upload_to='news_images', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.CharField(blank=True, max_length=12, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_image',
            field=models.ImageField(blank=True, upload_to='news_images', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_title',
            field=models.CharField(max_length=128, verbose_name='краткое название'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(blank=True, verbose_name='полное название'),
        ),
    ]