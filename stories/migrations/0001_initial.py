# Generated by Django 4.2.15 on 2024-08-25 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Published')], default=0)),
                ('journal_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='journal.journalentry')),
            ],
        ),
    ]
