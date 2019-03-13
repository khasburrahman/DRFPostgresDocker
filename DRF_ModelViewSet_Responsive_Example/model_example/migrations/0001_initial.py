# Generated by Django 2.1.7 on 2019-03-13 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('fielda', models.CharField(max_length=50)),
                ('fieldb', models.CharField(max_length=50)),
                ('fieldc', models.CharField(max_length=50)),
            ],
        ),
    ]
