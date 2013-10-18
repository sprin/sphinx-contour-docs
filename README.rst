===================
sphinx-contour-docs
===================

Install
-------

Clone and install::

  git clone https://github.com/sprin/sphinx-contour-docs.git
  cd sphinx-contour-docs
  python setup.py install
  

Enable Extension
----------------

Append to the extensions list in ``conf.py``::

    extensions = ['contour_docs.contour_docs']


Configure
---------

Set config variable to the projectID in ``conf.py`` file::

    CONTOUR_PROJECT_ID = 1111

    
Usage
-----

Link to a document with docID 111111::

    :contour:`111111`
    
