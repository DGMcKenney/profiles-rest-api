from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello_viewset')
router.register('profile', views.UserProfileViewSet)
# when using a model viewset, don't need to specify base name (third arg in line 6)
router.register('login', views.LoginViewSet, 'login')
router.register('feed', views.UserProfileFeedViewSet) # model viewset

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
