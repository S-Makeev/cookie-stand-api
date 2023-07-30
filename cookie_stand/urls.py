from django.urls import path
from .views import CookieStandlist, CookieStandDetail


urlpatterns = [
    path('', CookieStandlist.as_view(), name='cookie_list'),
    path('<int:pk>', CookieStandDetail.as_view(), name='cookie_detail')
]