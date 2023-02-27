"""Test sphinxcontrib.icon extension."""

import pytest
from bs4 import BeautifulSoup, formatter

fmt = formatter.HTMLFormatter(indent=2, void_element_close_prefix=" /")


@pytest.mark.sphinx("text", testroot="btn")
def test_btn_epub(app, status, warning):
    """Build a epub output (unsuported)."""
    app.builder.build_all()

    assert "Unsupported output format (node skipped)" in warning.getvalue()


@pytest.mark.sphinx("latex", testroot="btn")
def test_btn_latex(app, status, warning):
    """Build an icon role in Latex."""
    app.builder.build_all()

    result = (app.outdir / "test-btn.tex").read_text(encoding="utf8")

    assert r"\usepackage{fontspec}" in result
    assert r"\usepackage{tcolorbox}" in result
    assert (
        r"\newtcbox{\sphinxbtn}[1][]{box align=base, nobeforeafter, size=small, boxsep=2pt, #1}"
        in result
    )

    assert r'\sphinxbtn{{\solid\symbol{"F07B}} fa-folder}' in result
    assert r'\sphinxbtn{{\solid\symbol{"F07B}}}' in result
    assert r"\sphinxbtn{fa-folder}" in result


@pytest.mark.sphinx("html", testroot="btn")
def test_btn_html(app, status, warning, file_regression):
    """Build a btn role in HTML."""
    app.builder.build_all()

    html = (app.outdir / "index.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")

    complete = html.select("span.guilabel")[0].prettify(formatter=fmt)
    file_regression.check(complete, basename="complete_btn", extension=".html")

    icon = html.select("span.guilabel")[1].prettify(formatter=fmt)
    file_regression.check(icon, basename="icon_btn", extension=".html")

    title = html.select("span.guilabel")[2].prettify(formatter=fmt)
    file_regression.check(title, basename="title_btn", extension=".html")
