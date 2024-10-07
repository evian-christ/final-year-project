import os
import sys
import django
from pathlib import Path

# Add the path to your Django project
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'futforall.settings'
django.setup()

# -- General configuration ---------------------------------------------------

project = 'futforall'
author = 'Chan Kim'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinxcontrib_django',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'django': ('https://docs.djangoproject.com/en/stable/', 'https://docs.djangoproject.com/en/stable/_objects/'),
}

templates_path = ['_templates']
exclude_patterns = ['_build']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for sphinxcontrib-django ----------------------------------------

django_settings = 'futforall.settings'
django_apps = ['match', 'notifc', 'futforall', 'account']

autodoc_mock_imports = ["django"]

autodoc_default_flags = ['members', 'undoc-members', 'private-members', 'special-members', 'inherited-members']