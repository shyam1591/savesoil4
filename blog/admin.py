from django.contrib import admin
from .models import Photocontest, Post, Topic, Comment


class PhotocontestAdmin(admin.ModelAdmin):
    """Filter for Photocontest model"""

    list_display = (
        "name",
        "email",
        "submitted",
    )

    list_filter = (
        "name",
        "email",
        "submitted"
    )

class CommentAdmin(admin.ModelAdmin):
    """Search and display and filter setting for Comment model"""

    list_display = (
        "name",
        "email",
        "post",
        "active",
    )
    readonly_fields = ["name", "email", "post"]

    search_fields = ("post",)

    list_filter = ("active",)


class CommentInline(admin.TabularInline):
    """Comment inline in post model"""

    model = Comment


class TopicAdmin(admin.ModelAdmin):
    """Search and filter for Topic model"""

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    """Search and filter list for Post model"""

    list_display = (
        "title",
        "created",
        "updated",
    )

    inlines = [CommentInline]

    search_fields = (
        "title",
        "author__username",
        "author__first_name",
        "author__last_name",
    )

    list_filter = ("status", "topics")

    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Photocontest,PhotocontestAdmin)
