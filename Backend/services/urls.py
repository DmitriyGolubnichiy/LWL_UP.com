
from django.urls import path

from services.views import training_programs,basket_add,basket_remove

app_name = 'services'

urlpatterns = [
    path("", training_programs ,name='index' ),
    path("baskets/add/<int:service_id>/", basket_add ,name='basket_add' ),
    path("baskets/remove/<int:basket_id>/", basket_remove ,name='basket_remove' ),
]