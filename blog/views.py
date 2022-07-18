from django.shortcuts import render
from django.db.models import Count
from . import models

# Create your views here.
def home(request):
    """Blog home page"""

    all_topics = models.Topic.objects.order_by()
    # allpost = models.Post.objects.all().annotate(commentcount=Count("topics"))

    context = {"all_topics": all_topics}

    return render(request, "blog/home.html", context)
