# Generated by Django 4.0.5 on 2022-06-13 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inhabitant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=264)),
                ('first_mane', models.CharField(blank=True, max_length=264, null=True)),
                ('last_name', models.CharField(blank=True, max_length=264, null=True)),
                ('e_mail', models.EmailField(blank=True, max_length=264, null=True)),
                ('flat_area', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_title', models.CharField(max_length=264)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SingleVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_choice', models.CharField(choices=[('TAK', 'TAK'), ('NIE', 'NIE'), ('WSTRZYMUJE SIE', 'WSTRZYMUJE SIE')], max_length=50)),
                ('inhabitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NaszeOsiedle.inhabitant')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NaszeOsiedle.vote')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('inhabitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NaszeOsiedle.inhabitant')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('inhabitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NaszeOsiedle.inhabitant')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NaszeOsiedle.post')),
            ],
        ),
    ]