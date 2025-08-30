import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
import importlib.metadata

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'logngraph'
copyright = '2025, Vadim Gladushev'
author = 'Vadim Gladushev'
release = importlib.metadata.version("logngraph")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# Include all members, including variables
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'inherited-members': False,
    'show-inheritance': True,
    'special-members': '__init__',
}

# Include variables in autosummary tables
autosummary_generate = True

# For type hints
autodoc_typehints = "description"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_context = {
    'extra_nav_links': {
        'Special Thanks': 'thanks.html',
    }
}
