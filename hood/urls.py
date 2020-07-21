from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('edit_profile/(<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),
    path('companies',views.companies,name = 'companies'),
    path('post/(<id>\d+)',views.post,name='post'),
    path('search/',views.search,name='search'),
    path('api/companies/',views.CompanyList.as_view())

]