# Generated by Django 4.1.1 on 2022-10-22 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                ("image", models.ImageField(upload_to="building")),
                ("price", models.IntegerField()),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
                ("goodname", models.CharField(max_length=50)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
                ("image", models.ImageField(upload_to="city")),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Building_images",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.ImageField(upload_to="buildings")),
                ("index", models.IntegerField()),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.building"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="building",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.category"
            ),
        ),
        migrations.AddField(
            model_name="building",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.city"
            ),
        ),
    ]
