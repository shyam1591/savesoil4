from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponseRedirect
from . import models
from .forms import Photocontestform


# Create your views here.
# def home(request):
#     """Blog home page"""

#     all_topics = models.Topic.objects.order_by()
#     # allpost = models.Post.objects.all().annotate(commentcount=Count("topics"))

#     context = {"all_topics": all_topics}

#     return render(request, "blog/home.html", context)

def photo_contest(request):
    """View method"""
    submitted = False # if some visit the page for first time
    if request.method == "POST":
        form = Photocontestform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/PhotoContest?sub=True')
    else:
        form = Photocontestform
        if 'sub' in request.GET:
            submitted = True
    return render(request, 'blog/contest_form.html',{'form':form,'submitted':submitted})

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(kwargs)
        context["pt"] = models.Post.objects.filter(
            topics__slug=self.kwargs["slug"]
        ).order_by("-published")
        print(context["pt"])
        return context