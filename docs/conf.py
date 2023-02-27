"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup ----------------------------------------------------------------
from datetime import datetime

from sphinxcontrib.btn import __author__, __version__

# -- Project information -------------------------------------------------------

project = "sphinx-btn"
copyright = f"2020-{datetime.now().year}, {__author__}"
author = __author__
release = __version__


# -- General configuration -----------------------------------------------------

extensions = [
    "sphinx.ext.imgconverter",
    "sphinx_copybutton",
    "sphinxcontrib.icon",
    "sphinxcontrib.btn",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ---------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_context = {
    "github_user": "sphinx-contrib",
    "github_repo": "btn",
    "github_version": "main",
    "doc_path": "docs",
}
html_theme_options = {
    "logo": {"text": project},
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sphinx-contrib/btn",
            "icon": "fa-brands fa-github",
        }
    ],
}
