from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
