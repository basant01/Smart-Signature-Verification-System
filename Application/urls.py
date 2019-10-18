from django.urls import path,include
from Application.views import *

urlpatterns = [
	path('api/test/',func_hello),
	path('home/',home),

]
