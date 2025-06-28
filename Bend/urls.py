from django.urls import path
from Bend import views
urlpatterns=[
    path('login/',views.login,name="login"),
    path('logsave/',views.logsave,name="logsave"),
    path('signout/',views.signout,name="signout"),
    path('index/',views.index,name="index"),
    path('empadd/',views.empadd,name="empadd"),
    path('empsave/',views.empsave,name="empsave"),
    path('empdetails/',views.empdetails,name="empdetails"),
    path('empedit/<int:dataid>/',views.empedit,name="empedit"),
    path('updatedata/<int:dataid>/',views.updatedata,name="updatedata"),
    path('empdelete/<int:dataid>/',views.empdelete,name="empdelete"),
    path('catadd/',views.catadd,name="catadd"),
    path('catsave/',views.catsave,name="catsave"),
    path('catdetails/',views.catdetails,name="catdetails"),
    path('catedit/<int:dataid>/',views.catedit,name="catedit"),
    path('catupdate/<int:dataid>/',views.catupdate,name="catupdate"),
    path('catdelete/<int:dataid>/',views.catdelete,name="catdelete"),
    path('proadd/',views.proadd,name="proadd"),
    path('prosave/',views.prosave,name="prosave"),
    path('prodetails/',views.prodetails,name="prodetails"),
    path('proedit/<int:dataid>/',views.proedit,name="proedit"),
    path('proupdate/<int:dataid>/',views.proupdate,name="proupdate"),
    path('prodelete/<int:dataid>/',views.prodelete,name="prodelete"),
    path('regdetails/',views.regdetails,name="regdetails"),
    path('contactdetails/',views.contactdetails,name="contactdetails"),
    path('contactdlt/<int:dataid>/',views.contactdlt,name="contactdlt"),


]