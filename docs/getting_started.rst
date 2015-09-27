.. _getting_started:


***************
Getting started
***************

.. _installing-docdir:

.. image:: _static/pmi_rsz.png
    :scale: 100 %

Setting up Sphinx for documenting source-to-experiment simulation
=================================================================

You need clone the simS2E repository from GitHub::

  git clone https://github.com/chuckie82/start-to-end.git

The index.rst is the master ReST for your project.

You may already have `sphinx <http://sphinx.pocoo.org/>`_
installed -- you can check by doing::

  python -c 'import sphinx'

If that fails install the latest version with::

  > sudo easy_install -U Sphinx

Let's see if we can build our html::

  make html

If you now open your favorite internet browser and type :file:`_build/html/index.html`, you
should see the documentation website.

To update the document on the web, just push your changes::

   git add *.rst
   git commit -m "Update all documents"
   git push -u origin master

.. image:: _static/undulator_rsz.png
    :scale: 100 %




