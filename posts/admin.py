from django.contrib import admin
from .models import Post
# 客製化admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'creator', 'create_at'] #顯示欄位
    list_filter = ['category'] #右方篩選
    search_fields = ['title', 'content'] #上方搜尋欄位
# admin.site.register(Post, PostAdmin)
