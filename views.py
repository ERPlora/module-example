"""
Views for Example Module.

This module demonstrates how to create views for ERPlora Hub modules.

Key features:
- Uses @login_required to protect views
- Uses @htmx_view for SPA navigation support
- Renders templates from example/templates/example/
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view


@login_required
@htmx_view('example/pages/index.html', 'example/partials/content.html')
def index(request):
    """
    Main view for Example Module.

    Returns context dict that will be passed to the template.
    The @htmx_view decorator handles rendering the appropriate template:
    - Full page (pages/index.html) for direct browser requests
    - Partial (partials/content.html) for HTMX requests
    """
    return {
        'current_section': 'example',
        'page_title': 'Example Module',
    }


# Ejemplo de API endpoint
@login_required
@require_http_methods(["GET"])
def api_status(request):
    """
    Ejemplo de API endpoint.

    Retorna el estado del plugin en formato JSON.
    Útil para llamadas AJAX con HTMX o Alpine.js.

    Args:
        request: HttpRequest object

    Returns:
        JsonResponse: Estado del plugin

    Example:
        GET /example/api/status/

        Response:
        {
            "success": true,
            "plugin": "example",
            "version": "0.1.0",
            "status": "active"
        }
    """
    return JsonResponse({
        'success': True,
        'plugin': 'example',
        'version': '0.1.0',
        'status': 'active'
    })


# Agregar más vistas según necesites:
# - Formularios (crear, editar, eliminar)
# - APIs REST
# - Vistas de administración
# - Reportes
# - etc.
