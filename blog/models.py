from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.

class Photocontest(models.Model):
    """Model for PhotoContest"""

    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    image = models.ImageField(null = True, blank = True)
    submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define filtering order"""

        ordering = ['-submitted']

    def __str__(self):
        return self.name

### Topic Model ###
class Topic(models.Model):
    """Model for Topic"""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        """Have unique url for slug"""
        return reverse("topic-detail", kwargs={"slug": self.slug})

    class Meta:

        """Display order for topic"""

        ordering = ["name"]

    def __str__(self):
        """return method"""
        return self.name


### Post model ###
class Post(models.Model):
    """
    Model for blog post
    """

    topics = models.ManyToManyField(Topic, related_name="blog_posts")

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        null=True,
        blank=True,
        help_text="The date & time this article was published",
        unique_for_date="published",  # Slug is unique for publication date
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="blog_posts",
        null=True,
        blank=True,
    )

    DRAFT = "draft"
    PUBLISHED = " published"
    STATUS_CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date & time this article was published",
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )

    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    class Meta:
        """Define the order of post created"""

        ordering = ["-created"]

    def __str__(self):
        return self.title


### Comment Model ###
class Comment(models.Model):
    """Comment Model"""

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    class Meta:
        """Comment ordering"""

        ordering = ["-created"]

    def __str__(self):
        return self.name
