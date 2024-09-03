"""visittrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from visittrack_App.views import index  ,signup ,dashboard ,storeUser ,checkUser \
    ,newvisitor  ,managedept , logout ,storenewvisitor , view , \
        view_update ,update_data , delete_newvi ,store_dept ,viewdept , view_upd_dept ,update_dept ,del_dept ,\
            restoredept , restore_department ,delete_department , deletevisitor ,restore_newvi ,deleted_newvisitor , \
        profile ,updateprofile     
     
    

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name='index'),
    path("signup/",signup,name='signup'),
    path("dashboard/",dashboard,name='dashboard'),
    path("storeUser/",storeUser,name='storeUser'),
    path("checkUser/",checkUser,name='checkUser'),
    path("newvisitor/",newvisitor,name='newvisitor'),
    # path("managevisitor/",managevisitor,name='managevisitor'),
  #  path("bwdate/",bwdate,name='bwdate'),
    
    path("managedept/",managedept,name='managedept'),
    path("logout",logout,name='logout'),
    path("storenewvisitor/",storenewvisitor,name='storenewvisitor'),

    path('view/<int:vid>' , view, name='view'),
    path(' view_update/<int:vid>' , view_update, name='view_update'),
    path("update_data/",update_data,name='update_data'),
    path('delete_newvi/<int:vid>' , delete_newvi, name='delete_newvi'),
    path("store_dept/",store_dept,name='store_dept'),

    path('viewdept/<int:d_id>' ,viewdept, name='viewdept'),
    path('view_upd_dept/<int:d_id>' ,view_upd_dept, name='view_upd_dept'),
  
    path("update_dept/",update_dept,name='update_dept'),
    path('del_dept/<int:d_id>' ,del_dept, name='del_dept'),
    path("restoredept/",restoredept,name='restoredept'),

    path('restore_department/<int:d_id>' ,restore_department, name='restore_department'),
    path('delete_department/<int:d_id>' ,delete_department, name='delete_department'),
   
    path("deletevisitor/",deletevisitor,name='deletevisitor'),
    path('restore_newvi/<int:vid>' , restore_newvi, name='restore_newvi'),
    path('deleted_newvisitor/<int:vid>' , deleted_newvisitor, name='deleted_newvisitor'),


    path("profile/",profile,name='profile'),
    path("updateprofile/",updateprofile,name='updateprofile'),




    
]
