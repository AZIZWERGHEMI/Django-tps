from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import logout_view
from .views import CategoryAPIView
from rest_framework import routers
from magasin.views import CategoryAPIView
from .views import ProduitAPIView



urlpatterns = [
    path("", views.index, name="index"),
    path("majProduits/", views.produit, name="produit"),
    path("majFournisseurs/", views.fournisseur, name="fournisseur"),
    path("Commande/", views.commande, name="commande"),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    path('blog/', include('blog.urls')), 
     path('api/category/', CategoryAPIView.as_view()),
         path('api/produits/', ProduitAPIView.as_view())


 # Include the blog app's URLs

]
