# Example Module - Módulo de Ejemplo para ERPlora Hub

**Versión:** 0.1.0
**Autor:** ERPlora Team
**Descripción:** Módulo de ejemplo funcional que muestra cómo crear módulos para ERPlora Hub.

---

## 📋 ¿Qué es este módulo?

Este módulo es un **ejemplo completo y funcional** que demuestra cómo crear módulos para ERPlora Hub. Incluye:

✅ Estructura completa de archivos
✅ Página "Hello World" con Ionic components
✅ Ejemplo de Alpine.js para interactividad
✅ Modelo de datos comentado
✅ URLs configuradas
✅ Tests de ejemplo
✅ Documentación detallada
✅ Icono SVG personalizado

---

## 🚀 Instalación

Este módulo está incluido por defecto en el Hub para propósitos educativos (desactivado con prefijo `_`).

### Activar el módulo:

1. Ir al dashboard del Hub
2. Navegar a "Modules"
3. Activar "Example Module"
4. El módulo estará disponible en `/modules/example/`

---

## 📁 Estructura del Módulo

```
example/
├── module.json              # Metadata del módulo (nombre, versión, deps)
├── __init__.py              # Package init
├── apps.py                  # Configuración Django del módulo
├── models.py                # Modelos de datos (ejemplo comentado)
├── views.py                 # Vistas del módulo
├── urls.py                  # URLs del módulo
├── templates/
│   └── example/
│       └── index.html       # Template con Ionic + Alpine.js
├── static/
│   ├── icons/
│   │   └── icon.svg         # Icono del módulo (SVG preferido)
│   └── example/
│       ├── css/             # CSS personalizado
│       ├── js/              # JavaScript adicional
│       └── img/             # Imágenes del módulo
├── migrations/
│   └── __init__.py          # Migraciones de base de datos
├── management/
│   └── commands/            # Management commands personalizados
├── tests/
│   ├── __init__.py
│   └── test_example.py      # Tests del módulo
├── README.md                # Este archivo
└── .gitignore               # Archivos a ignorar
```

---

## 🎨 Iconos del Módulo

ERPlora soporta iconos SVG y PNG personalizados para módulos.

### Prioridad de iconos:

1. `static/icons/icon.svg` (preferido - inline, escalable)
2. `static/icons/icon.png` (alternativa - base64)
3. Campo `icon` en `module.json` (Ionic icon fallback)
4. `cube-outline` (default)

### Requisitos SVG:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Paths aquí -->
</svg>
```

- Usar `currentColor` para heredar color del CSS
- Tamaño recomendado: 24x24 viewBox
- Librerías gratuitas: [Lucide](https://lucide.dev), [Heroicons](https://heroicons.com), [Tabler](https://tabler-icons.io)

### Requisitos PNG:

- Dimensiones: 48x48 o 64x64 pixels
- Fondo transparente
- Tamaño archivo: < 10KB

---

## 🔧 Desarrollo

### Requisitos previos

- Python 3.11+
- Django 5.1+
- ERPlora Hub instalado

### Comandos útiles

```bash
# Activar entorno virtual
source .venv/bin/activate

# Crear migraciones (si agregaste modelos)
python manage.py makemigrations example

# Aplicar migraciones
python manage.py migrate example

# Ejecutar tests
pytest modules/example/tests/
```

---

## 📝 Crear un módulo desde cero

Usa este módulo como base para crear tus propios módulos:

### Copiar este módulo

```bash
# Copiar carpeta example
cp -r modules/_example modules/mi-modulo

# Editar archivos:
# 1. module.json - Cambiar module_id, name, author
# 2. apps.py - Cambiar nombre de clase
# 3. Renombrar carpetas templates/example → templates/mi-modulo
# 4. Renombrar carpetas static/example → static/mi-modulo
# 5. Añadir icono en static/icons/icon.svg
```

---

## 🎨 Componentes de UI

Este módulo usa:

- **Ionic 8**: Componentes UI profesionales (modo iOS)
- **Alpine.js**: Reactividad ligera sin framework pesado
- **HTMX**: Interactividad sin escribir mucho JavaScript
- **Tailwind CSS**: Utilidades CSS

### Ejemplo de componente Ionic:

```html
<ion-card>
  <ion-card-header>
    <ion-card-title>Título</ion-card-title>
  </ion-card-header>
  <ion-card-content>
    Contenido del card
  </ion-card-content>
</ion-card>
```

### Ejemplo de Alpine.js:

```html
<div x-data="{ count: 0 }">
  <ion-button @click="count++">
    Contador: <span x-text="count"></span>
  </ion-button>
</div>
```

---

## 📊 Modelos de Datos

Para crear modelos, edita `models.py`. **IMPORTANTE:** Usa prefijos en `db_table` para evitar conflictos:

```python
from django.db import models

class ExampleItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'example_item'  # Prefijo 'example_' es crucial
        ordering = ['-created_at']

    def __str__(self):
        return self.name
```

Después de crear modelos:

```bash
# Crear migración
python manage.py makemigrations example

# Aplicar migración
python manage.py migrate example
```

---

## 🔌 module.json

```json
{
  "module_id": "example",
  "name": "Example Module",
  "name_es": "Módulo de Ejemplo",
  "version": "0.1.0",
  "description": "Example module for ERPlora Hub",
  "description_es": "Módulo de ejemplo para ERPlora Hub",
  "author": "Your Name",
  "author_email": "your@email.com",
  "license": "MIT",
  "category": "general",
  "tags": ["example", "demo", "template"],
  "icon": "cube-outline",

  "dependencies": {
    "python": [],
    "modules": []
  },

  "compatibility": {
    "min_erplora_version": "1.0.0",
    "max_erplora_version": "2.0.0"
  },

  "menu": {
    "label": "Example",
    "label_es": "Ejemplo",
    "icon": "cube-outline",
    "order": 100,
    "url": "/modules/example/"
  },

  "permissions": [
    "example.view_exampleitem",
    "example.add_exampleitem",
    "example.change_exampleitem",
    "example.delete_exampleitem"
  ]
}
```

---

## 🧪 Testing

Crea tests en `tests/test_example.py`:

```python
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_example_view(client):
    """Test que la vista principal funciona"""
    url = reverse('example:index')
    response = client.get(url)
    assert response.status_code == 200
```

Ejecutar tests:

```bash
# Todos los tests del módulo
pytest modules/example/tests/

# Test específico
pytest modules/example/tests/test_example.py::test_example_view

# Con coverage
pytest modules/example/tests/ --cov=example
```

---

## 📚 Recursos

- [Documentación ERPlora Modules](../../docs/MODULE_ICONS.md)
- [Ionic Components](https://ionicframework.com/docs/components)
- [Alpine.js Docs](https://alpinejs.dev)
- [HTMX Docs](https://htmx.org/docs/)
- [Lucide Icons](https://lucide.dev)

---

## 📄 Licencia

MIT License

---

## ✍️ Autor

**ERPlora Team**
Email: support@erplora.com
Website: https://erplora.com

---

**Última actualización:** 2025-12-26
