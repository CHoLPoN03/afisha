# Generated by Django 5.1 on 2024-09-02 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars_alter_movie_duration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Directo',
            new_name='Director',
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_reviews', to='movie_app.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=5),
        ),
    ]
