from django.contrib import admin

from projects.models import Category, Image, \
                            Project, Status, Technology
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Project, MarkdownxModelAdmin)
admin.site.register(Status)
admin.site.register(Technology, MarkdownxModelAdmin)
