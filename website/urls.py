from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('product/<int:id>', views.product, name="product"),
    path('cart/', views.cart, name="cart"), 
    path('wishlist/', views.wishlist, name="wishlist"),
    path('adddel/<int:id>', views.adddel, name="adddel"),
    path('addcard/<int:id>', views.addcard, name="addcard"),
    path('whishlist2/<int:id>', views.whishlist2, name="whishlist2"),
    path('wishdel/<int:id>', views.wishdel, name="wishdel"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="register"),
    path('regdata/', views.regdata, name="regdata"),
    path('checkout/', views.checkout, name="checkout"),
    path('myacc/', views.myacc, name="myacc"),
    path('order/', views.order, name="order"),
    path('shop/', views.shop, name="shop"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)