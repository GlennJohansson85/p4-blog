from django.db import models
from django.utils import timezone
from profiles.models import Profile


class Post(models.Model):
    '''
    A model representing a post created by a user.
    '''
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img/posts', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True) 
     
    def __str__(self):
        """
        Returns post title.
        """
        return self.title

    def short_content(self):
        '''
        Returns post content.
        '''
        return self.content[:100]


class Comment(models.Model):
    '''
    A model representing a comment made on a post.
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        '''
        Returns users username and comment text.
        '''
        return f'{self.user.user_name} - {self.text}'