# Generated by Django 4.2.1 on 2023-06-02 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=128)),
                ("price", models.DecimalField(decimal_places=2, max_digits=3)),
                ("number_in_stock", models.PositiveBigIntegerField(default=0)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("C", "Crime"),
                            ("N", "Non Fiction"),
                            ("O", "Other"),
                            ("S", "Sci Fi"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.author"
                    ),
                ),
            ],
        ),
    ]