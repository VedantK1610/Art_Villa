from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('arts/',views.gallery,name='gallery'),
    path('photo/<int:pk>/',views.viewPhoto.as_view(),name='photo'),
    path('add/',views.addPhoto,name='add'),
    path('login/',views.loginpage,name='login'),
    path('section/',views.section),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('exit/',views.exit,name='exit'),
    # path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    #  path('cart/',views.show_cart,name='showcart'),
    #  path('checkout/',views.show_cart,name='checkout'),
      path('cart/',views.cart,name='cart'),
     path('checkout/',views.checkout,name='checkout'),
      path('update_item/',views.updateItem,name='update_item'),
      path('process_order/',views.processOrder,name='process_order'),
       path('aboutus/',views.aboutus,name='aboutus'),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #to fetch image from static/images
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 