from rest_framework.routers import DefaultRouter

from projects.views import ProjectsViewSet


router = DefaultRouter()
router.register("", ProjectsViewSet, basename="projects")

urlpatterns = router.urls
