from rest_framework.routers import DefaultRouter
from base.views.columns import ColumnsViewset
from base.views.cards import CardsViewset

router = DefaultRouter()
router.register(r'cards', CardsViewset, basename='cards')
router.register(r'columns', ColumnsViewset, basename='columns')

urlpatterns = router.urls
