from pathlib import Path

import pytest
from docutils import nodes

import sphinxcontrib.btn.btn as btn
from sphinxcontrib.btn.font_handler import Fontawesome


class TestBtn:
    def test_get_glyph(self, icons, data_dir):

        btn.font_handler = Fontawesome()
        btn.font_handler.download_asset("html", data_dir)

        # expected results
        expected_results = {
            "folder": ("fa", "folder"),
            "fas": ("fas", "ad"),
            "fa": ("fa", "save"),
            "far": ("far", "address-book"),
            "fab": ("fab", "github"),
        }

        # test the true icons
        for k, i in icons["true"].items():
            assert expected_results[k] == btn.get_glyph(i["icon"])

        # test the fake style
        with pytest.raises(ValueError) as e:
            btn.get_glyph(icons["false"]["fat"]["icon"])

        assert str(e.value) == 'invalid icon name: "fat fa-folder"'

        # test the fake icon
        # with pytest.raises(ValueError) as e:
        #    icon.get_glyph(icons["false"]["toto"]["icon"])
        #
        # assert str(e.value) == 'icon "toto" is not part of fontawesome 5.15.4'

    def test_visit_html(self, app, btn_list, data_dir):

        btn.font_handler = Fontawesome()
        btn.font_handler.download_asset("html", data_dir)

        expected_results = {
            "all": '<span class="guilabel"><i class="fa fa-check" style="margin-right: .5em;"></i>validate</span>',
            "icon": '<span class="guilabel"><i class="fa fa-globe" ></i></span>',
            "text": '<span class="guilabel"><i class="" ></i>version</span>',
        }

        for k, b in btn_list.items():
            btn.visit_btn_node_html(app, b)
            assert app.body.output == expected_results[k]

        return

    def test_visit_latex(self, app, btn_list, data_dir):

        btn.font_handler = Fontawesome()
        btn.font_handler.download_asset("latex", data_dir)

        # expecteed results for true the fixture inputs
        expected_results = {
            "all": "\\sphinxbtn{\\faIcon{check} validate}",
            "icon": "\\sphinxbtn{\\faIcon{globe}}",
            "text": "\\sphinxbtn{version}",
        }

        for k, b in btn_list.items():
            btn.visit_btn_node_latex(app, b)
            assert app.body.output == expected_results[k]

        # check that the package was added only once
        macro = (
            "\\usepackage{fontawesome5}\n"
            + "\\usepackage{tcolorbox}\n"
            + "\\newtcbox{\\sphinxbtn}[1][]{box align=base, nobeforeafter, size=small, boxsep=2pt, #1}\n"
        )
        assert app.elements["preamble"] == macro

        return

    def test_visit_unsuported(self, app, btn_list):

        # check that the appropiate error is raised
        with pytest.raises(nodes.SkipNode):
            btn.visit_btn_node_unsuported(app, btn_list["all"])

        return

    def test_icon_role(self, btn_list):

        # check that the node has the appropirate class
        _ = None
        node, messages = btn.btn_role(_, _, btn_list["all"]["icon"], _, _)

        assert isinstance(node[0], btn.btn)
        assert len(messages) == 0

        return

    @pytest.fixture
    def icons(self):
        return {
            "true": {
                "folder": {"icon": "fa fa-folder"},
                "fas": {"icon": "fas fa-ad"},
                "fa": {"icon": "fa fa-save"},
                "far": {"icon": "far fa-address-book"},
                "fab": {"icon": "fab fa-github"},
            },
            "false": {
                # "toto": {"icon": "fa fa-toto"},
                "fat": {"icon": "fat fa-folder"},
            },
        }

    @pytest.fixture
    def app(self):
        """mock the app builder for warning in fonctions."""

        class Builder:
            pass

        class Body:
            def append(self, str):
                self.output = str
                return

        class App:
            def __init__(self):
                self.builder = Builder()
                self.body = Body()
                self.elements = {"preamble": ""}

        return App()

    @pytest.fixture
    def data_dir(self):

        data_dir = Path(__file__).parent / "data"

        return data_dir

    @pytest.fixture
    def btn_list(self):
        """all possible combination of btn."""
        return {
            "all": {"icon": "fa fa-check", "text": "validate"},
            "icon": {"icon": "fa fa-globe", "text": ""},
            "text": {"icon": "", "text": "version"},
        }
