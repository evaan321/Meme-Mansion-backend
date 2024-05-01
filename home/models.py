from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    categoryName = models.CharField(max_length = 12)

    def __str__(self) -> str:
        return self.categoryName
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    commentField = models.TextField()
    commentTime = models.DateTimeField(auto_now_add = True)




class Meme(models.Model):
    user = models.ForeignKey(User, on_delete =models.SET_NULL,null = True,blank=True)
    title = models.CharField(max_length = 50,blank=True)
    category = models.ManyToManyField(Category, blank= True )
    postTime = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to='image',blank=True)
    comments = models.ManyToManyField(Comment,blank= True)
    likes = models.ManyToManyField(User,blank=True,related_name='liked_memes')
    

    def __str__(self) -> str:
        return self.title




