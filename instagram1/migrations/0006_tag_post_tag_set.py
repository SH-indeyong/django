# Generated by Django 4.2 on 2023-07-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram1", "0005_post_author_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tag_set",
            field=models.ManyToManyField(blank=True, to="instagram1.tag"),
        ),
    ]