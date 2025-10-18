# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'OOP'
copyright = '2025, Victoria Kalion, Pauline Gorozhankina, Anna Zubrilina'
author = 'Victoria Kalion, Pauline Gorozhankina, Anna Zubrilina'
release = '19.10.2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Автоматическая документация из кода
    'sphinx.ext.viewcode',   # Показ исходного кода
    'sphinx.ext.napoleon',   # Поддержка Google-style docstrings
]


templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
