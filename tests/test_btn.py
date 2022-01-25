from docutils import nodes
from pathlib import Path
import pytest

import sphinxcontrib.btn.btn as btn
from sphinxcontrib.btn.font_handler import Fontawesome


class TestIcon:
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

    def test_visit_html(self, app, icons, data_dir):

        btn.font_handler = Fontawesome()
        btn.font_handler.download_asset("html", data_dir)

        for i in icons["true"].values():
            btn.visit_icon_node_html(app, i)
            assert app.body.output == f'<i class="{i["icon"]}"></i>'

        for i in icons["false"].values():
            with pytest.raises(nodes.SkipNode):
                btn.visit_icon_node_html(app, i)

        return

    def test_visit_latex(self, app, icons, data_dir):

        btn.font_handler = Fontawesome()
        btn.font_handler.download_asset("latex", data_dir)

        # expecteed results for true icons
        expected_results = {
            "folder": "\\faIcon{folder}",
            "fas": "\\faIcon[solid]{ad}",
            "fa": "\\faIcon{save}",
            "far": "\\faIcon[regular]{address-book}",
            "fab": "\\faIcon[brand]{github}",
        }

        for k, i in icons["true"].items():
            btn.visit_icon_node_latex(app, i)
            assert app.body.output == expected_results[k]

        # check that the package was added once
        assert app.elements["preamble"] == "\\usepackage{fontawesome5}\n"

        return

    def test_visit_unsuported(self, app, icons):

        # check that the appropiate error is raised
        with pytest.raises(nodes.SkipNode):
            btn.visit_icon_node_unsuported(app, icons["true"]["folder"])

        return

    def test_icon_role(self, icons):

        # check that the node has the appropirate class
        _ = None
        node, messages = btn.icon_role(_, _, icons["true"]["folder"], _, _)

        assert isinstance(node[0], btn.icon)
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
        """mock the app builder for warning in fonctions"""

        class Builder:
            def warn(self, str):
                print(str)
                return

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
