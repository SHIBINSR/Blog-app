from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default="")
    title = models.CharField(max_length=200,default="")
    short_desc = models.CharField(max_length=300,default="")
    content = RichTextField(blank=True, null=True,)
    tumbnail = models.ImageField(upload_to="blogimages")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Comments(models.Model):
    name = models.CharField(max_length=180,default="")
    blogparent = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Reply(models.Model):
    name = models.CharField(max_length=180,default="")
    commentparent = models.ForeignKey(Comments,on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
