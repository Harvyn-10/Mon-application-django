# Generated by Django 5.0.3 on 2024-03-31 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RailExpress', '0002_alter_train_heure_arrivée_alter_train_heure_départ'),
    ]

    operations = [
        migrations.CreateModel(
            name='trains',
            fields=[
                ('IDTrain', models.AutoField(primary_key=True, serialize=False)),
                ('Plan', models.CharField(max_length=400)),
                ('Destination', models.CharField(max_length=100)),
                ('Datetime', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=300)),
                ('Cover', models.CharField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='train',
        ),
    ]
