from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
import pytz
from datetime import timedelta


class Post(models.Model):
    author = models.ForeignKey('auth.User' ,related_name='author_post', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = RichTextField(blank = True, null=True)

    tz1 = pytz.timezone('Asia/Kolkata')
    current_time = timezone.now().astimezone(tz1)
    duration = timedelta(hours=5, minutes=30)
    current_date = current_time + duration
    created_date = models.DateTimeField(default=current_date)

    published_date = models.DateTimeField(blank=True, null=True)
    post_img = models.ImageField(upload_to='images', blank = True)

    def publish(self):
        tz = pytz.timezone('Asia/Kolkata') 
        current_time = timezone.now().astimezone(tz)
        duration = timedelta(hours=5, minutes=30)
        current_date = current_time + duration
        self.published_date = current_date
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title




class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete= models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    tz = pytz.timezone('Asia/Kolkata') 
    current_time = timezone.now().astimezone(tz)
    duration = timedelta(hours=5, minutes=30)
    current_date = current_time + duration
    create_date = models.DateTimeField(default=current_date)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('post_list')
    

# Create your models here.
