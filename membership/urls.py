from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dash/', views.dash, name='dash'),
    path('about/', views.about, name='about'),
    path('sigs/', views.sigs, name='sigs'),
    path('my_conf/<int:user_id>/', views.my_conferences, name='my_conf'),
    path('my_cpds/', views.my_cpds, name='my_cpds')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
