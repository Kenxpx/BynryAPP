import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django_application = get_asgi_application()

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    "http": django_application,
    # Add WebSocket/other protocol handlers here
})