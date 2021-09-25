from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    url = models.URLField(default="www.theopengears.com")
    date_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True,blank=True)
    takeaway_One = models.CharField(max_length=100, null=True,blank=True)
    takeaway_Two = models.CharField(max_length=100, null=True,blank=True)
    takeaway_Three = models.CharField(max_length=100, null=True,blank=True)


    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

class FAQ (models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=255,null=True)

class Events(models.Model):
    date=models.CharField(max_length=255)
    description=models.TextField()
    guestSpeaker=models.CharField(max_length=255)

COLOR_CHOICES=(
    ('events','EVENTS'),
    ('socialmedia','SOCIALMEDIA'),
    ('speakers','SPEAKERS'),
    ('logistics','LOGISTICS'),
    ('other','OTHER'),
)
class Feedback(models.Model):
    option=models.CharField(max_length=11,choices=COLOR_CHOICES,default='events')
    suggestion=models.CharField(max_length=350)
