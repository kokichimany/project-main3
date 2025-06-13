from django.contrib import admin
from .models import Product, Category, Comment, Post, PostComment
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostComment)

admin.site.site_header = 'Админка'
admin.site.site_title = 'Аниме магазин'
admin.site.index_title = 'Добро пожаловать в панель управление'
