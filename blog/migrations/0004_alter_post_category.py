# Generated by Django 4.2.3 on 2023-07-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='Null', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
