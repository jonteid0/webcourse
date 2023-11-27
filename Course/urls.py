from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include('core.urls')),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('questions/<int:category_id>/', views.question_list, name='question_list'),
]
