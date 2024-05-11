from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import BlogSerializer
from django.views.generic.edit import CreateView
from rest_framework.response import Response

class ListePostes(ListView):
    model = Post
    template_name = 'blog/liste_postes.html'

class DetailPoste(DetailView):
    model = Post
    template_name = 'blog/detail_poste.html'


class CreerPost(CreateView):
    model = Post
    template_name = 'blog/creer_post.html'
    fields = ['title', 'content', 'status', 'slug', 'image']

    success_url = reverse_lazy('liste_postes')

    def form_valid(self, form):
        form.instance.author = self.request.user

        self.object = form.save()
        return super().form_valid(form)

class ModifierPoste(UpdateView):
    model = Post
    template_name = 'blog/modifier_poste.html'
    fields = ['title', 'content', 'status', 'image']
    success_url = reverse_lazy('liste_postes')

class SupprimerPoste(DeleteView):
    model = Post
    template_name = 'blog/supprimer_poste.html'
    success_url = reverse_lazy('liste_postes')

class BlogAPIView(APIView):
    def get(self, *args, **kwargs):
        Blogs = Post.objects.all()
        serializer = BlogSerializer(Blogs, many=True)
        return Response(serializer.data)

class BlogViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = Post.objects.filter()
        blog_Id = self.request.GET.get('author_id')
        if blog_Id:
            queryset = queryset.filter(blog_id=blog_Id)
        return queryset