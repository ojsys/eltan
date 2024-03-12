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
    path('my_cpds/', views.my_cpds, name='my_cpds'),

    #Conference Registration
    path('conference_registration/<int:conference_id>', views.conference_registration, name='conference_register'),
    path('user/conferences/', views.user_conferences, name='user_conferences'),

    #Update Profile
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/update/success/', views.profile_update_success, name='profile_update_success'),

    #Download Certificate
    path('download_certificate/my_certs', views.view_certs, name='my_certs'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
