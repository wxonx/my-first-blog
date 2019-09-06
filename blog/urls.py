{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]