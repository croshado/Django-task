from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('submissions/', views.submissions, name='submissions'),
    path('delete_submission/<int:id>/', views.delete_submission, name='delete_submission'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
