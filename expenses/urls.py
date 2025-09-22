from django.urls import path

from . import views


app_name = "expenses"

urlpatterns = [
    path("", views.expense_list, name="list"),
    path("add/", views.expense_create, name="add"),
    path("<int:pk>/edit/", views.expense_update, name="edit"),
    path("<int:pk>/delete/", views.expense_delete, name="delete"),
    path("summary/", views.expense_summary, name="summary"),
]


