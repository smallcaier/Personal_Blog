from django.contrib import admin
from .models import ArticlePost
from .models import ArticleColumn

# 注册文章栏目
admin.site.register(ArticleColumn)
#将articlePost注册到admin中
admin.site.register(ArticlePost)
