from django.urls import path,include
from .import views 

urlpatterns = [
    path ('',views.index, name='index'),
    path ('mybloggs/',views.my_bloggs,name='mybloggs'),
    path ('loging/',views.logging,name='logging'),
    path ('signup/',views.register_view,name='signup'),
    path ('blogger/',views.blogger,name='blogger'),
    path ('newPost/',views.newPost,name='new_post'),
    path ('post_dlt/<int:id>',views.post_del,name='post_delete'),
    path ('update/<int:id>',views.Post_update,name='post_update'),
    path ('update_data/<int:id>',views.Post_tp_value,name='post_update_value'),
    path('add_comment/',views.add_comment, name='add_comment'),
    path('profile/',views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout')
    
]