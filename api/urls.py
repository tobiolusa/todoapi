from django.urls import path 
from .import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
  
)


urlpatterns = [
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path( '', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name = "task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name = "task-detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name = "task-update"),
    path('task-create/', views.create, name="task-create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete")
     
]
