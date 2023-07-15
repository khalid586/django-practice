from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "ShopHome"),
    path("about/",views.about,name = "AboutUs"),
    path("contact/",views.contact,name = "contact"),
    path("checkout/",views.checkout,name = "checkout")
]