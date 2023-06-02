from rest_framework.routers import DefaultRouter

from polls.views import PollsViewSet

router = DefaultRouter()
router.register('polls', PollsViewSet, basename='polls')
urlpatterns = [

]
urlpatterns += router.urls