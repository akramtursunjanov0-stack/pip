
from django.contrib import admin
from django.urls import path
from films import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(openapi.Info(
    title="Films API",
    default_version='v1',
    description='API для филмов',
),
public=True,
permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/films/', views.film_list_api_view),
    path('api/v1/films/<int:id>/',views.film_detail_api_view),
    



    #Swagger 
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0)),

]
