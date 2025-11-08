from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('',views.test),
    path('index',views.index),
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),


    path('',include(router.urls)),

]
