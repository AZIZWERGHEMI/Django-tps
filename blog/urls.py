from django.urls import path
from .views import ListePostes, DetailPoste, CreerPost, ModifierPoste, SupprimerPoste
from blog.views import BlogAPIView

urlpatterns = [
    path('liste/', ListePostes.as_view(), name='liste_postes'),
    path('<int:pk>/', DetailPoste.as_view(), name='detail_poste'),
    path('creer_post/', CreerPost.as_view(), name='creer_post'), 
    path('<int:pk>/modifier/', ModifierPoste.as_view(), name='modifier_poste'),
    path('<int:pk>/supprimer/', SupprimerPoste.as_view(), name='supprimer_poste'),
    path('api/Post/', BlogAPIView.as_view()),

]
