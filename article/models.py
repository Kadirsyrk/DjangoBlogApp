from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar")
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True,verbose_name = "Oluşturma Tarihi")
    article_image = models.FileField(blank = True , null= True,verbose_name="Makaleye Fotoğraf ekleyin")
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name = "comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    profile_picture = models.ImageField(upload_to='comment_profile_pictures/', null=True, blank=True)


    def __str__(self):
        return self.comment_content
