# Generated by Django 2.1 on 2018-12-16 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='webapp.User', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('Ужасно', 'Ужасно'), ('Плохо', 'Плохо'), ('Нормально', 'Нормально'), ('Хорошо', 'Хорошо'), ('Отлично', 'Отлично')], default='Нормально', max_length=20, verbose_name='оценка'),
        ),
    ]