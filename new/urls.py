from django.urls import path
from shop import views
from .views import new_product,about,contact,accessories,merchandise,vouchers,repairs

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('new_product/', new_product, name='new_product'),
    path('accessories/', accessories, name='accessories'),
    path('merchandise/', merchandise, name='merchandise'),
    path('article_list/', merchandise, name='article_list'),
    path('vouchers/', vouchers, name='vouchers'),
    path('repairs/', repairs, name='repairs'), 
]