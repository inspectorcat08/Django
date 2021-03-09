from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Name - {self.name}, Author - {self.author}'


class CommentToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(null=True, blank=True)
    comment_to_comment = models.ForeignKey('myapp.CommentToArticle', null=True, blank=True,
                                           on_delete=models.DO_NOTHING,
                                           related_name='comments')
    created_at = models.DateField(default=date.today())

    def save(self, **kwargs):
        if not self.id:
            self.created_at = date.today() - relativedelta(years=1)
        super().save(**kwargs)

    def __str__(self):
        if self.comment_to_comment:
            return f'Comment by {self.author.name} ({self.comment}) ' \
                   f'to another comment ({self.comment_to_comment.comment}) ' \
                   f'under Article "{self.article.name}"'
        else:
            return f'Comment by {self.author.name} ({self.comment}) ' \
                   f'to Article "{self.article.name}"'


class LikeToComment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_comments_likes')
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE, related_name='comments_likes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.author} to {self.comment}'


class DislikeToComment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_comments_dislikes')
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE, related_name='comments_dislikes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dislike by {self.author} to {self.comment}'


class LikeToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_articles_likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_likes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.author} to Article "{self.article.name}'


class DislikeToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_articles_dislikes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles_dislikes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dislike by {self.author} to Article "{self.article.name}"'


