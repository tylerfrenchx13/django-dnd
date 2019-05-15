# Generated by Django 2.2.1 on 2019-05-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('subtitle', models.CharField(max_length=16)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Alignments',
            },
        ),
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('prerequisite', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Feats',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('speakers', models.CharField(max_length=64)),
                ('script', models.CharField(default='---', max_length=8)),
                ('exotic', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age_range', models.CharField(help_text='Range for when the races are considered adults. Lower values are accepted.', max_length=12)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('speed', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Races',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, help_text='Value in gold pieces.', max_digits=10)),
                ('name', models.CharField(max_length=32)),
                ('set', models.CharField(choices=[("Artisan's Tools", "Artisan's Tools"), ('Gaming Set', 'Gaming Set'), ('General', 'General'), ('Musical Instrument', 'Musical Instrument')], max_length=16)),
                ('weight', models.DecimalField(decimal_places=2, help_text='Value in pounds.', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Character Name')),
                ('level', models.IntegerField(default=1, verbose_name='Level')),
                ('character_class', models.CharField(max_length=20, verbose_name='Class')),
                ('background', models.TextField(blank=True, null=True, verbose_name='Background')),
                ('player_name', models.CharField(max_length=50, verbose_name='Players Name')),
                ('race', models.CharField(choices=[('Dragonborn', 'Dragonborn'), ('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Gnome', 'Gnome'), ('Half Elf', 'Half Elf'), ('Half Orc', 'Half Orc'), ('Halfling', 'Halfling'), ('Human', 'Human'), ('Tiefling', 'Tiefling')], max_length=20, verbose_name='Race')),
                ('alignment', models.CharField(max_length=50, verbose_name='Alignment')),
                ('experience_points', models.PositiveIntegerField(default=0, verbose_name='Experience Points')),
            ],
            options={
                'unique_together': {('name', 'character_class', 'race', 'player_name')},
            },
        ),
    ]