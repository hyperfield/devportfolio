from django.contrib import admin

from .models import Update, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'created_on')


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')


admin.site.register(Update, UpdateAdmin)
admin.site.register(Comment, CommentAdmin)
