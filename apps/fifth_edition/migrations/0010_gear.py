# Generated by Django 3.0.2 on 2020-03-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifth_edition', '0009_weapon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('cost', models.IntegerField(help_text='Value in gold pieces.')),
                ('weight', models.DecimalField(decimal_places=2, help_text='Weight in pounds.', max_digits=10)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Gear',
            },
        ),
        migrations.AlterField(
            model_name='armor',
            name='weight',
            field=models.DecimalField(decimal_places=2, help_text='Weight in pounds.', max_digits=10),
        ),
    ]
