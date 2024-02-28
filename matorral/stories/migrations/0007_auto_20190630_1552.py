# Generated by Django 2.2.1 on 2019-06-30 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stories", "0006_auto_20190526_1241"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalstory",
            old_name="owner",
            new_name="requester",
        ),
        migrations.RemoveField(
            model_name="story",
            name="owner",
        ),
        migrations.AddField(
            model_name="story",
            name="requester",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="requested_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
