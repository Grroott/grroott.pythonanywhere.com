# Generated by Django 3.0.7 on 2020-06-20 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_remove_profile_lives_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followed',
            field=models.ManyToManyField(blank=True, default=None, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_value', models.CharField(choices=[('Follow', 'Follow'), ('Following', 'Following')], default='Follow', max_length=10)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
