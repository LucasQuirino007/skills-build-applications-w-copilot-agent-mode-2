import os

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.decorators import api_view
from rest_framework.response import Response

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = 'http://localhost:8000'


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'users': f'{base_url}/api/users/',
            'teams': f'{base_url}/api/teams/',
            'activities': f'{base_url}/api/activities/',
            'leaderboard': f'{base_url}/api/leaderboard/',
            'workouts': f'{base_url}/api/workouts/',
        }
    )

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False), name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('octofitcore.urls')),
]
