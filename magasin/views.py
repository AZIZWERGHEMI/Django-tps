from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produit, Commande
from django.template import loader
from .forms import ProduitForm, FournisseurForm, CommandeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
from .models import Fournisseur

def logout_view(request):
    logout(request)
    # Rediriger vers la page de connexion ou une autre page spécifiée après la déconnexion
    return redirect('login')  # Assurez-vous de remplacer 'login' par le nom de l'URL de la page de connexion

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Bienvenue {username}, votre compte a été créé avec succès !')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    produit = Produit.objects.all()
    context = {"produit": produit}
    return render(request, "magasin/vitrine.html", context)


def produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/magasin")
    else:
        form = ProduitForm()
    return render(request, "magasin/majProduits.html", {"form": form})




def fournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/magasin")
    else:
        form = FournisseurForm()
    listFour = Fournisseur.objects.all()

    return render(request, "magasin/majFournisseurs.html", {"form": form , 'fournisseurs':listFour})


def commande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/magasin")
    else:
        form = CommandeForm()
        produit = Commande.objects.all()
        context = {"produit": produit}
    commandes = Commande.objects.all()

    return render(request, "magasin/Commande.html", {"form": form ,'commandes':commandes})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from magasin.models import Categorie, Produit
from magasin.serializers import CategorySerializer, ProduitSerializer

class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProduitAPIView(APIView):
    def get(self, request, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Produit.objects.filter(active=True)
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
