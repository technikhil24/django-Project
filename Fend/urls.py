from django.urls import path
from Fend import views
urlpatterns=[
    path('home/',views.home,name="home"),
    path('discategory/<itemCatg>',views.discategory,name="discategory"),
    path('products/',views.products,name="products"),
    path('prodetails/<int:dataid>',views.prodetails,name="prodetails"),
    path('contact/',views.contact,name="contact"),
    path('reglog/',views.reglog,name="reglog"),
    path('logdata/',views.logdata,name="logdata"),
    path('regdata/',views.regdata,name="regdata"),
    path('logout/',views.logout,name="logout"),
    path('contactsave/',views.contactsave,name="contactsave"),
    path('cart/',views.cart,name="cart"),
    path('prodetailsave/',views.prodetailsave,name="prodetailsave")

]