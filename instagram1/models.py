from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag_set = models.ManyToManyField('Tag', blank=True)
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to="instagram1/post/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString 기능
    def __str__(self):
        return f"Custom Post object ({self.id})"
        # return self.message

    def get_absolute_url(self):
        return reverse("instagram1:post_detail", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ["-id"]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # post_id 필드 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name