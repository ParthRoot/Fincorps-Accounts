from django.urls import path
from . import views
#from. models import views
urlpatterns = [
    path('', views.index, name="index"),
    path('report', views.report, name="report"),
    path('gl', views.gl, name="gl"),
    path('home', views.home, name="home"),
    path('add_account', views.add_account, name="add_account"),
    path('login', views.login, name="login"),
    path('login_ex', views.login_ex, name="login_ex"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    
    #data entry
    path('general_ledger_entry', views.general_ledger_entry, name="general_ledger_entry"),
    
    #retrive_gl_data
    path('retrive_gl_data', views.retrive_gl_data, name="retrive_gl_data")
    
]