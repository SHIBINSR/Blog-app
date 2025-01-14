from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="Home"),
    path("about",views.about,name="About"),
    path("contact",views.contact,name="Contact"),
    path("contentreading/<str:id>",views.contentreading,name="Contentreading"),
    path("signup",views.signup,name="Signup"),
    path("login",views.Login,name="Login"),
    path("logout",views.Logout,name="Logout"),
    path("comment",views.comment,name="Comment"),
    path("reply",views.reply,name="Reply"),  
]
