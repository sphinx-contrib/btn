sphinx-btn
==========

Overview
--------

:code:`sphinx-btn` is a Sphinx extention to allow developers to use the :code:`btn` role to display inlined btn in their documentation. A btn is composed of an icon and/or some text.
The extention currently supports only Fontawsome 5.15.4 icons.
Please go to our `doc <https://sphinx-btn.readthedocs.io/en/latest/>`__ if you want to know more.

Contribute
^^^^^^^^^^

If you want to contribute you can fork the project in you own repository and then use it. 
If you consider working with us, please follow the `contributing guidelines <https://github.com/sphinxcontrib/btn/blob/main/CONTRIBUTING.rst>`__. 
Meet our `contributor <https://github.com/sphinxcontrib/btn/blob/main/AUTHORS.rst>`__. 

Installation
------------

first install the `pipy package <https://pypi.org/project/sphinx-btn/>`__ by runinng:

.. code-block:: console

    pip install sphinx-btn

Then add the extention to your :code:`conf.py` file:

.. code-block:: python

    # docs/conf.py

    # [...]

    # -- General configuration -----------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
        "sphinxcontrib.btn",
    ]

Usage
-----

This module provides support for including inlined fontawesome btn in Sphinx rst documents.

This module defines the :code:`btn` role to display inlined btn in their documentation. A btn is composed of an icon and/or some text.
The extention currently supports only Fontawsome 5.15.4 icons. You'll find the complete list of available icons on the `fontawesome website <https://fontawesome.com/v5.15/icons?d=gallery&p=2>`__. the strcuture of the role is the following: 

.. code-block:: rst 

    :btn:`<icon_name> the_text`

.. note::

    :code:`icon_name` or :code:`the_text` can be ommitted. If the :code:`icon_name` is ommitted make sure that you also removed the :code:`<` and :code:`>`.

Example
^^^^^^^

Build a sentence with a button with text and icon: 

.. code-block:: rst

    When the form is complete click on :btn:`<fa fa-check> send`

which will render as: When the form is complete click on :btn:`<fa fa-check> send`

Build a sentence with only an icon: 

.. code-block:: rst

    Click on :btn:`<fa fa-globe>` to see the map.

Which will render as: Click on :btn:`<fa fa-globe>` to see the map.

Finally it can only be text: 

.. code-block:: rst

    Click :btn:`version` to open the version dropdown.

Which will render as: Click :btn:`version` to open the version dropdown

HTML output
-----------

In the HTML output, the CSS and JS from Fontawesome 5.15.4 are added to the output in the :code:`<head>` tag.

.. code-block:: html 

    <link rel="stylesheet" type="text/css" href="_font/fontawesome/css/all.min.css">
    <!-- -->
    <script src="_font/fontawesome/css/all.min.js">

Then for each btn role occurence an :code:`<span>` tag will be used: 

.. code-block:: html

    <span class="guilabel"><i class="icon_name"></i>the_text</span>

Latex output
------------

In the latex outut the `fontawesome5 <https://www.ctan.org/pkg/fontawesome5>`__ and `tcolorbox <https://www.ctan.org/pkg/tcolorbox>`__ packages are added to the :code:`preamble`:

.. code-block:: Latex

    \usepackage{fontawesome5}
    \usepackage{tcolorbox}

Then a prestyled macro is created from :code:`tcolorbox`:

.. code-block:: latex

    \newtcbox{\sphinxbtn}[1][]{box align=base, nobeforeafter, size=small, boxsep=2pt, #1}

Finally for each btn role occurence the following command will be used: 

.. code-block:: latex

    \sphinxbtn{\faIcon[style]{icon_name} the_text}"

with :code:`style` being one of "regular", "solid" or "brand" and :code:`icon_name` being everything after :code:`fa-`.
