"""Btn extention to embed icon in sphinx guilabels outputs."""

from typing import Any, Dict
from textwrap import dedent

from sphinx.application import Sphinx
from sphinx.config import Config

from .btn import _NODE_VISITORS, Btn, btn_node

__version__ = "0.1.0"
__author__ = "Pierrick Rambaud"
__email__ = "pierrick.rambaud49@gmail.com"

def tbox_handler(app: Sphinx, config: Config) -> None:
    """add the tbox command to preamble"""

    if "preamble" not in config.latex_elements:
            config.latex_elements["preamble"] = ""

    config.latex_elements["preamble"] += dedent(
        r"\newtcbox{\sphinxbtn}[1][]{box align=base, nobeforeafter, size=small, boxsep=2pt, #1}"
    )


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add btn node to the sphinx builder."""
    # load the btn node/role
    app.add_node(btn_node, **_NODE_VISITORS)  # type: ignore
    app.add_role("btn", Btn())

    # install latex files and extentions
    app.add_latex_package("tcolorbox")
    app.connect("config-inited", tbox_handler)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
