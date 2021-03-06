===============================
basicBlogWeb
===============================

Python project of Milo

Development
-----------

1. Clone basic-blog-web::

    git clone git@github.com:milojing/basic-blog-web.git

2. Navigate into the project directory::

    cd basic-blog-web

3. Setup project::

    python setup.py develop

   or(use install, you need to do this every time when you change the code)::

    python setup.py install


Launch basic-blog-web
~~~~~~~~~~~~~~~~~~~~~
Launch basicblogweb directly with command::

    bbw

Run Test Suite
~~~~~~~~~~~~~~

The test suite is using py.test internally::

    python setup.py test

Or directly with pytest::

    py.test tests

Create Coverage Report
~~~~~~~~~~~~~~~~~~~~~~

To get a detailed test report::

    py.test tests --cov=basicblogweb

Create html report::

    py.test tests --cov=basicblogweb --cov-report=html

Run standardize testing with tox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute tox::

    tox

Create documentation
~~~~~~~~~~~~~~~~~~~~

To create documentation in docs by using sphinx(>1.3)::

    make.bat html

Control the version of project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To change the version of project by using bumpversion(default major, minor, patch)::

    bumpversion minor
