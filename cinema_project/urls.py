from django.contrib import admin
from django.urls import path , include
from films import views
from rest_framework.routers import DefaultRouter
from films.views import FilmViewSet
from . import swagger


router = DefaultRouter()
router.register('films',FilmViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/films/', views.film_list_api_view),
    path('api/v1/films/<int:id>/',views.film_detail_api_view),
    path('api/v1/users/', include('users.urls')),
    path('api/v2/', include(router.urls)),    
]


urlpatterns += swagger.urlpatterns