from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#Leave as empty string for base url
	path('', views.main, name="main"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)