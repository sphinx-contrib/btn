# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup ----------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))

from sphinxcontrib.btn import __author__, __version__


# -- Project information -------------------------------------------------------

project = "sphinx-btn"
copyright = f"2020-{datetime.now().year}, {__author__}"
author = __author__

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.imgconverter",
    "sphinx_copybutton",
    "sphinxcontrib.spelling",
    "sphinxcontrib.btn",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**.ipynb_checkpoints"]


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"


# -- Options for spelling output -----------------------------------------------
spelling_lang = "en_US"
spelling_show_suggestions = True
spelling_verbose = False
