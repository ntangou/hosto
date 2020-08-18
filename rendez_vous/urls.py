from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns =[
    path('rdv/', views.rdv, name='rdv'),
    path('rdv/qrcode/<int:id>', cache_page(60 * 15)(views.qrcode), name='qrcodeindex'),  
]

