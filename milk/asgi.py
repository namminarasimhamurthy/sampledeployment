import os
from django.core.asgi import get_asgi_application
from mangum import Mangum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "milk.settings")

application = get_asgi_application()

# ✅ THIS IS THE KEY FIX
app = Mangum(application)
