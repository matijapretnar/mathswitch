# Generated by Django 4.2.6 on 2023-10-27 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='links',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='concepts.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]