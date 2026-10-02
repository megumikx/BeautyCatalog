from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.product_list,
        name="product_list"
    ),

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "brands/",
        views.brand_list,
        name="brand_list"
    ),

    path(
        "review/<int:pk>/edit/",
        views.review_edit,
        name="review_edit"
    ),

    path(
        "review/<int:pk>/delete/",
        views.review_delete,
        name="review_delete"
    ),
]