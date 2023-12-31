# Generated by Django 4.2.5 on 2023-09-24 08:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('phoneNumber', models.CharField(max_length=200, null=True)),
                ('was_online', models.DateTimeField(default=django.utils.timezone.now)),
                ('recent_reaction_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=200, unique=True)),
                ('message_content', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('react_emoji', models.CharField(max_length=200, null=True)),
                ('react_count', models.CharField(max_length=200, null=True)),
                ('bot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bot', to='bot.botuser')),
            ],
        ),
    ]
