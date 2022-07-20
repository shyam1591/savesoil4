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

    template_name = "blog/topic_detail.html"
    model = models.Topic
    # context_object_name = "post_topic"
    # print(models.Post.objects.filter(topics=1))

    # def get_queryset(self):
    #     # tps = models.Topic.objects.filter(slug=self.kwargs.get("slug"))
    #     # tps = models.Post.objects.filter(topics__slug=self.kwargs.get("slug"))
    #     print(models.Topic.objects.filter(blog_posts__topics=self.kwargs.get("slug")))

    #     return models.Topic.objects.filter(blog_posts__topics=self.kwargs.get("slug"))

    # def get_object(self, **kwargs):
    #     print(kwargs)
    #     return models.Topic.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(kwargs)
        context["pt"] = models.Post.objects.filter(
            topics__slug=self.kwargs["slug"]
        ).order_by("-published")
        print(context["pt"])
        return context
