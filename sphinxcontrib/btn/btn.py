"""The btn role definition."""

import re
from typing import List, Tuple

from docutils import nodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxRole, SphinxTranslator

from sphinxcontrib.icon import icon

logger = logging.getLogger(__name__)


class btn_node(nodes.General, nodes.Element):
    """The btn node."""

    pass


class Btn(SphinxRole):
    """The Btn sphinxrole interpreter."""

    def run(self) -> Tuple[List[nodes.Node], List[str]]:
        """Setup the role in the builder context."""
        m = re.match("^(?P<icon><.+>)?(?P<title>.*)?$", self.text)
        if not m:
            logger.warning("btn role cannot be empty")
            raise nodes.SkipNode

        # split icon and text parameters in 2 variables
        icon = m.group("icon") or ""
        title = m.group("title") or ""

        # build the node with sanitized strings
        node = btn_node(
            icon=icon.replace("<", "").replace(">", ""),
            title=title.strip(),
            location=self.get_source_info(),
        )

        return [node], []


def visit_btn_node_html(translator: SphinxTranslator, node: btn_node) -> None:
    """Visit the html node."""
    # open the html output
    translator.body.append('<span class="guilabel">')

    # add the icon if existing
    if node["icon"]:
        icon_node = icon.icon_node(icon=node["icon"], location=node["location"])
        icon.visit_icon_node_html(translator, icon_node)
        icon.depart_icon_node_html(translator, icon_node)

    # add the title if existing
    if node["title"]:
        margin = 'style="margin-left: .5em;"' if node["icon"] else ""
        translator.body.append(f'<span {margin}>{node["title"]}</span>')


def depart_btn_node_html(translator: SphinxTranslator, node: btn_node) -> None:
    """Depart of the html node."""
    translator.body.append("</span>")


def visit_btn_node_latex(translator: SphinxTranslator, node: btn_node) -> None:
    """Visit of the latex node."""
    # open the command
    translator.body.append(r"\sphinxbtn{")

    # add the icon if existing
    if node["icon"]:
        icon_node = icon.icon_node(icon=node["icon"], location=node["location"])
        icon.visit_icon_node_latex(translator, icon_node)
        icon.depart_icon_node_latex(translator, icon_node)

    # add the title if existing
    if node["title"]:
        margin = " " if node["icon"] else ""
        translator.body.append(r"%s%s" % (margin, node["title"]))


def depart_btn_node_latex(translator: SphinxTranslator, node: btn_node) -> None:
    """Depart of the latex node."""
    translator.body.append(r"}")


def visit_btn_node_unsuported(translator: SphinxTranslator, node: btn_node) -> None:
    """Raise error when the requested output is not supported."""
    logger.warning(
        "Unsupported output format (node skipped)", location=node["location"]
    )
    raise nodes.SkipNode


_NODE_VISITORS = {
    "html": (visit_btn_node_html, depart_btn_node_html),
    "latex": (visit_btn_node_latex, depart_btn_node_latex),
    "man": (visit_btn_node_unsuported, None),
    "texinfo": (visit_btn_node_unsuported, None),
    "text": (visit_btn_node_unsuported, None),
}
