
from django.shortcuts import render
from rssapp.models import URL
from django.http import request

from rest_framework import viewsets,generics
from .serializers import URLSerializer
from .models import URL

import feedparser


from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class API_objects(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


###############################

class URLListView(ListView):
    model = URL
    template_name = 'list.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(URLListView, self).get_context_data(**kwargs)
        urls = self.get_queryset()
        context['list'] = urls
        return context



class BookDetailView(DetailView):

    model = URL
    template_name = 'detail.html'
    context_object_name = 'url'


class UrlUpdateView(UpdateView):

    model = URL
    template_name = 'update.html'
    context_object_name = 'url'
    fields = ('urlinput', 'id',)

    def get_success_url(self):
        return reverse('url-detail', kwargs={'pk': self.object.id})


class UrlCreateView(CreateView):
    model = URL
    template_name = 'create.html'
    fields = ('urlinput', 'id', )
    success_url = reverse_lazy('url-list')


class BookDeleteView(DeleteView):
    model = URL
    template_name = 'delete.html'
    success_url = reverse_lazy('url-list')

############################################

def index(request):
    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data
        list =URL.objects.all()
    else:
        feed = None
        list = URL.objects.all()
    return render(request, 'reader.html', {"feed" : feed, "list": list})

