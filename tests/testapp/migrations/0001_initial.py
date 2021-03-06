# Generated by Django 2.0.4 on 2018-04-12 07:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import feincms3_sites.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("feincms3_sites", "0002_site_is_managed_re")]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                (
                    "category",
                    models.CharField(
                        choices=[("publications", "publications"), ("blog", "blog")],
                        max_length=20,
                        verbose_name="category",
                    ),
                ),
            ],
            options={"ordering": ["-pk"]},
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "application",
                    models.CharField(
                        blank=True,
                        choices=[("publications", "publications"), ("blog", "blog")],
                        max_length=20,
                        verbose_name="application",
                    ),
                ),
                (
                    "app_instance_namespace",
                    models.CharField(
                        editable=False,
                        max_length=100,
                        verbose_name="app instance namespace",
                    ),
                ),
                (
                    "menu",
                    models.CharField(
                        blank=True,
                        choices=[("main", "main"), ("footer", "footer")],
                        default="main",
                        max_length=20,
                        verbose_name="menu",
                    ),
                ),
                (
                    "template_key",
                    models.CharField(
                        choices=[
                            ("standard", "standard"),
                            ("with-sidebar", "with sidebar"),
                        ],
                        default="standard",
                        max_length=100,
                        verbose_name="template",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        choices=[("en", "English"), ("de", "German")],
                        default="en",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "redirect_to_url",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Redirect to URL"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is active"),
                ),
                ("title", models.CharField(max_length=200, verbose_name="title")),
                ("slug", models.SlugField(verbose_name="slug")),
                (
                    "position",
                    models.PositiveIntegerField(
                        db_index=True, default=0, editable=False
                    ),
                ),
                (
                    "static_path",
                    models.BooleanField(default=False, verbose_name="static path"),
                ),
                (
                    "path",
                    models.CharField(
                        blank=True,
                        help_text="Generated automatically if 'static path' is unset.",
                        max_length=1000,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Path must start and end with a slash (/).",
                                regex="^/(|.+/)$",
                            )
                        ],
                        verbose_name="path",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="testapp.Page",
                    ),
                ),
                (
                    "redirect_to_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="testapp.Page",
                        verbose_name="Redirect to page",
                    ),
                ),
                (
                    "site",
                    feincms3_sites.models.SiteForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="feincms3_sites.Site",
                        verbose_name="site",
                    ),
                ),
            ],
            options={
                "verbose_name": "page",
                "verbose_name_plural": "pages",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Snippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "template_name",
                    models.CharField(
                        choices=[("snippet.html", "snippet")],
                        max_length=200,
                        verbose_name="template name",
                    ),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testapp_snippet_set",
                        to="testapp.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "snippet",
                "verbose_name_plural": "snippets",
                "abstract": False,
            },
        ),
        migrations.AlterUniqueTogether(name="page", unique_together={("site", "path")}),
    ]
