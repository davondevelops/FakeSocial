from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register',views.register),
    path('register/create', views.create),
    path('login/validate', views.validate),
    path('homepage', views.homepage),
    path('logout', views.logout),
    path('edit/account', views.editAccount),
    path('edit/submit', views.update),
    path('create/quote', views.createQuote),
    path('view/<int:x>/quotes', views.viewQuotes),
    path('delete/quote/<int:x>', views.deleteQuote), 
    path('liked/quote/<int:x>', views.likeQuote)
]
