==========================
templer.django-project-app
==========================

.. contents::

Introduction
============

This package extends the functionality of the templer code generation
system. It builds upon the functionality of templer.core_, and depends on
that package.

Templer.django-project-app provides basic support for creating Django
applications within an existing project like the ``startproject`` command
but in a more useful way.


Getting the code
================

For the latest stable version of the package use `easy_install` or `pip`: ::

  $ easy_install templer.django-project-app
  $ pip install templer.django-project-app

You could also retrieve the development version of the module like this: ::

  $ pip install -e git://github.com/Fantomas42/templer.django-project-app.git#egg=templer.django-project-app

Creating applications
=====================

As with the parent package, templer.core, creating packages using
templer.django-project-app template is accomplished by using the
``templer`` script. The script is invoked thus: ::

  $ templer django_project_app

This will create a basic application skeleton related to your project,
containing the models.py, urls.py and views.py which may be edited to
taste.

Changelog
=========

1.1
---

* Pep8 on the code.
* Fix model's meta verbose names.

1.0
---

* Using class-based views.
* Adding structure for management commands.
* Completing the default model and admin classes.

0.1.1
-----

* Creation of a ``tests.py`` file.
* The model name is now configurable.
* Rename ``project`` var to ``project_root``.
* Add a post run message with instructions for installing the new created
  applications.

0.1
---

* Porting the code of the unreleased *paster.django_project_application* to
  *templer.django-project-app*.


.. _templer.core: http://pypi.python.org/pypi/templer.core
