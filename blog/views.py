from multiprocessing import context
from os import supports_effective_ids
from pydoc_data.topics import topics
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from django.db.models import Count
from . import models

# Create your views here.
# def home(request):
#     """Blog home page"""

#     all_topics = models.Topic.objects.order_by()
#     # allpost = models.Post.objects.all().annotate(commentcount=Count("topics"))

#     context = {"all_topics": all_topics}

#     return render(request, "blog/home.html", context)


class HomeView(TemplateView):
    """Class based view for Home tab"""

    template_name = "blog/home.html"


class TopicListView(ListView):
    """List view of Topic Model"""

    # template_name = "topic_list.html"

    model = models.Topic
    context_object_name = "list_topics"
    queryset = models.Topic.objects.order_by("name")


class TopicDetailView(DetailView):
    """Detial view for Topic"""

    # template_name = "topic_detail.html"
    model = models.Topic
    context_object_name = "post_topic"
    queryset: models.Topic.objects.all()

    # def get_context_data(self, **kwargs):
    #     Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     Add in a QuerySet of all the books
    #     context["tp_list"] = models.Post.objects.all()
    #     return context
