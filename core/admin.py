from django.contrib import admin
from core.models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content', 'tags__name')
    list_filter = ['tags']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)