from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class Inhabitant(AbstractBaseUser):

    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=264)
    first_name = models.CharField(max_length=264, null=True, blank=True)
    last_name = models.CharField(max_length=264, null=True, blank=True)
    e_mail = models.EmailField(max_length=264, null=True, blank=True)
    flat_area = models.DecimalField(max_digits=5, decimal_places=2)


class Vote(models.Model):

    def __str__(self):
        return self.vote_title
    vote_title = models.CharField(max_length=264)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(help_text='dd.mm.rrrr, --:--')


class SingleVote(models.Model):
    class Meta:
        unique_together = ("inhabitant", "vote")

    class VoteChoice(models.TextChoices):
        yes = "TAK", "TAK"
        no = "NIE", "NIE"
        pauses = "WSTRZYMUJE SIE", "WSTRZYMUJE SIE"

    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    inhabitant = models.ForeignKey(Inhabitant, on_delete=models.CASCADE)
    vote_choice = models.CharField(max_length=50, choices=VoteChoice.choices)


class Post(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    inhabitant = models.ForeignKey(Inhabitant, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    image = models.ImageField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    inhabitant = models.ForeignKey(Inhabitant, on_delete=models.CASCADE)




