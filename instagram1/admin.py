from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# Register your models here.

# 등록법 1
# admin.site.register(Post)


# 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Post, PostAdmin)


# 등록법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ['pk']   # primarykey = id
    list_display = [
        "id",
        'photo_tag',
        "message",
        "message_length",
        "is_public",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["message"]
    list_filter = ["created_at", "is_public"]
    search_fields = ["message"]

    def message_length(self, post):
        return f"{len(post.message)} 글자"

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px"/>')
        return None

    message_length.short_description = "메세지 글자 수"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass