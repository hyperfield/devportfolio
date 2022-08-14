from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=25)
    description = MarkdownxField()

    class Meta:
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.title


class Status(models.Model):
    status_name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.status_name


class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img_projects')
    project = models.ForeignKey('Project', on_delete=models.PROTECT,
                                null=True, blank=True)

    class Meta:
        verbose_name_plural = "images"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=25, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    url_name = models.CharField(max_length=247, null=True, blank=True)
    src_url = models.URLField(max_length=255, null=True, blank=True)
    src_url_name = models.CharField(max_length=247, null=True, blank=True)
    short_description = MarkdownxField(null=True)
    long_description = MarkdownxField(null=True)
    technologies = models.ManyToManyField(Technology)
    gallery = models.ManyToManyField(Image, related_name='galleries')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)

    @property
    def markdown_long_description(self):
        return markdownify(self.long_description)

    class Meta:
        verbose_name_plural = "projects"

    def __str__(self):
        return self.title
