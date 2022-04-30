from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="ToDo Woo API",
      default_version='v1',
      description="Connecting API to a todo app",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kramstyles@outlook.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('todos/', views.TodoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>', views.TodoUpdate.as_view(), name='todo-create'),
    path('todos/<int:pk>/ok', views.TodoOk.as_view(), name='todo-ok'),
    path('completed/', views.TodoCompletedList.as_view(), name='todo-completed'),

    # API DOCUMENTATION
    path('json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
