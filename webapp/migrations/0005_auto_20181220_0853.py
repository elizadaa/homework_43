# Generated by Django 2.1.4 on 2018-12-20 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20181216_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('mark', models.CharField(choices=[('Ужасно', 'Ужасно'), ('Плохо', 'Плохо'), ('Нормально', 'Нормально'), ('Хорошо', 'Хорошо'), ('Отлично', 'Отлично')], default='Нормально', max_length=25, verbose_name='оценка')),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='article',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='article',
            name='commented_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.AddField(
            model_name='article',
            name='comment_by',
            field=models.ManyToManyField(related_name='comment_by', through='webapp.Comment', to='webapp.User', verbose_name='Комментарий пользователя'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favored_by', to='webapp.Article', verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='article',
            name='rated_by',
            field=models.ManyToManyField(related_name='rated_by', through='webapp.Mark', to='webapp.User', verbose_name='Оценки пользователя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='user',
            name='commented_articles',
            field=models.ManyToManyField(related_name='comments_articles', through='webapp.Comment', to='webapp.Article', verbose_name='Комментированные'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rated_articles',
            field=models.ManyToManyField(related_name='rated_articles', through='webapp.Mark', to='webapp.Article', verbose_name='Оцененные'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.AddField(
            model_name='mark',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mark', to='webapp.Article'),
        ),
        migrations.AddField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mark', to='webapp.User'),
        ),
    ]
