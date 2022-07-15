from django.urls import path
from api import views

urlpatterns = [
    path("",views.ListapiAPIView.as_view(),name="api_list"),
    # path("create/", views.CreateapiAPIView.as_view(),name="api_create"),
    # path("update/<int:pk>/",views.UpdateapiAPIView.as_view(),name="update_api"),
    # path("delete/<int:pk>/",views.DeleteapiAPIView.as_view(),name="delete_api")
]