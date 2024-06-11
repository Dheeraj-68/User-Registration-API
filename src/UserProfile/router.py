from rest_framework import routers

from .viewsets import UserViewset,ProfileViewset

app_name = 'UserProfile'

router = routers.DefaultRouter()
router.register('users',UserViewset)
router.register('profiles',ProfileViewset)