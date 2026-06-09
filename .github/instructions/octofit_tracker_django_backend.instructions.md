---
applyTo: "octofit-tracker/backend/**"
---
# Diretrizes do Backend Django da App de Fitness Octofit-tracker

## Estrutura da App Backend Django

### settings.py

Should always contain the following:

```python
import os
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

## serializers.py

```text
serializers devem converter campos ObjectId para strings
```

## Endpoints da REST API

```text
use curl para testar os endpoints
```

### urls.py

Should always use the codespace environment variable for the URL

```python
import os
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
```