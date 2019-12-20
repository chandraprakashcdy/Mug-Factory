from django.urls import path, include
from django.conf.urls import include
from rest_framework import routers
from .views import (
     MugDetail, MugList, MugStaff
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'home'
urlpatterns = [
    path('mug/', MugList.as_view()),
    #path('mug/<category>/', MugSearch.as_view()),
    #path('mug/search/', MugSearch.as_view()),
    path('mug/<int:pk>/', MugDetail.as_view()),
    path('mug/mugstaff/<int:pk>', MugStaff.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
