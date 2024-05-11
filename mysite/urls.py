from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView

router = routers.SimpleRouter()
router.register(r'produit', ProductViewset, basename='produit')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("magasin/", include("magasin.urls")),
    path('blog/', include('blog.urls')),  # Include the blog app's URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('api/', include(router.urls)),
    path('api/produit/get_products_by_category_id/', ProductViewset.as_view({'get': 'get_products_by_category_id'}), name='produit-get-products-by-category-id'),
    path('api/produit/<int:pk>/', ProductViewset.as_view({'get': 'retrieve_product'}), name='produit-retrieve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
