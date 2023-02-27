Quickstart
==========

This section contains basic information about **sphinx-btn** to get you started.

Installation
------------

Use ``pip`` to install **sphinx-btn** in your environment:

.. code-block:: console

    pip install sphinx-btn

Extension setup
---------------


After installing **sphinx-btn**, add ``sphinxcontrib.icon`` and ``sphinxcontrib.btn`` to the list of extensions
in your ``conf.py`` file:

.. code-block:: python

    extensions = [
        #[...]
        "sphinxcontrib.icon",
        "sphinxcontrib.btn"
    ]

.. note::

    The **sphinx-btn** extention rely on **sphinx-icon** to provide access to the fontawesome 6.3.0 icons font/metadata.

Icon directive
--------------

You can now add buttons directly in your documentation:

.. code-block:: rst

    I'm a :btn:`<fa-solid fa-folder> fa-folder` btn.
    I'm a :btn:`<fa-solid fa-folder>` btn.
    I'm a :btn:`fa-folder` btn.

I'm a :btn:`<fa-solid fa-folder> fa-folder` btn.

I'm a :btn:`<fa-solid fa-folder>` btn.

I'm a :btn:`fa-folder` btn.

.. note::

    Support is provided for older version of Fontawesome. Documentation using ``fas|far|fab`` or ``fa`` will continue working. Be aware that the icon you want to use may changed name since then.

HTML output
-----------

In the HTML output, the CSS and JS from Fontawesome 6.3.0 are added to the output in the ``<head>`` tag.

.. code-block:: html

    <link rel="stylesheet" type="text/css" href="<webpath>/build/html/_font/fontawesome/css/all.min.css">
    <!-- -->
    <script src="<webpath>/build/html/_font/fontawesome/css/all.min.js">

Then for each btn role occurence an ``<span>`` of class ``guilabel`` tag will be used:

.. code-block:: html

    <span class="guilabel">
        <i class="fa-solid fa-folder"></i>
        <span style="margin-left: .5em;">fa-folder</span>
    </span>


Latex output
------------

For the latex output, the **sphinx-btn** extention need to use the webfonts provided by fontawesome. It will thus force the use of the XeLaTex builder to allow use of the `fontspec <https://ctan.org/pkg/fontspec?lang=en>`__ and `tcolorbox <https://www.ctan.org/pkg/tcolorbox>`__ packages. Then 3 new font will be added to the preamble of the tex file as well as a ``sphinxbtn`` command:

.. code-block:: latex

    \newfontfamily{\solid}{fa-solid-900.ttf}
    \newfontfamily{\regular}{fa-regular-400.ttf}
    \newfontfamily{\brands}{fa-brands-400.ttf}

    \newtcbox{\sphinxbtn}[1][]{box align=base, nobeforeafter, size=small, boxsep=2pt, #1}

Then for each btn role occurence the following command will be used:

.. code-block:: latex

    \sphinxbtn{{\solid\symbol{"F07B}} fa-folder}

where ``solid`` is the font style selected in the role and ``F007`` being the unicode of the selected icon.
