from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("salt", models.CharField(max_length=255)),
                ("passwd", models.CharField(max_length=255)),
                ("time", models.CharField(max_length=255)),
                ("isdelete", models.BooleanField(default=False)),
                ("avatar", models.CharField(max_length=255)),
            ],
        ),
    ]
