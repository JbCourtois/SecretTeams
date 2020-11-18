from django.urls import path, re_path

import smartteams.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        '<slug:seed>/<slug:teams>/<int:player>/<int:game>',
        views.generate, name="generate",
    ),
]
