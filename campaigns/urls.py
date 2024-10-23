
"""
# campaigns/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('campaign/<int:pk>/', views.campaign_detail, name='campaign_detail'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:pk>/pledge/', views.pledge_campaign, name='pledge_campaign'),
]
"""


"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("campaigns/",views.campaign_list,name='campaign_list'),
    path('campaigns/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:pk>/', views.campaign_detail, name='campaign_detail'),
    path('campaign/<int:pk>/pledge/', views.pledge_campaign, name='pledge_campaign'),
]
"""



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('campaigns/', views.campaign_list, name='campaign_list'),  # View all campaigns
    path('create_campaign/', views.create_campaign, name='create_campaign'),  # Create a new campaign
    path('campaign/<int:pk>/', views.campaign_detail, name='campaign_detail'),  # View specific campaign details
    path('campaign/<int:pk>/pledge/', views.pledge_campaign, name='pledge_campaign'),  # Pledge to a campaign
]
