from django.contrib import admin
from .models import Author, Article, CommentToArticle, LikeToComment, \
    DislikeToComment, LikeToArticle, DislikeToArticle

# чтобы изменять действия которые внутри (дополнительные поля и тд) - необязательное
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
# class BookAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(CommentToArticle)
admin.site.register(LikeToComment)
admin.site.register(DislikeToComment)
admin.site.register(LikeToArticle)
admin.site.register(DislikeToArticle)