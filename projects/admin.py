from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin
from adminsortable2.admin import SortableInlineAdminMixin
from adminsortable2.admin import SortableAdminMixin

from projects.models import Category, Image, \
                            Project, Status, Technology


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class ProjectInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Project
    # readonly_fields = ("file_image", )

    # def file_image(self, obj):
    #   return format_html('<img src="{}" style="max-height: 200px">',
    #                        obj.file.url)


admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Status)
admin.site.register(Technology, MarkdownxModelAdmin)
