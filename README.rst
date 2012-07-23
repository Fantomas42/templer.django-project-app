==========================
templer.django-project-app
==========================

.. contents::

Introduction
============

This package extends the functionality of the templer code generation
system. It builds upon the functionality of templer.core_, and depends on
that package.

This package provides basic support for creating Django applications within
an existing project.

Creating Applications
=====================

As with the parent package, templer.core, creating packages using
templer.django-project-app template is accomplished by using the
``templer`` script. The script is invoked thus: ::

  $ templer django_project_app

This will create a basic application skeleton related to your project,
containing the models.py, urls.py and views.py which may be edited to
taste.

.. _templer.core: http://pypi.python.org/pypi/templer.core
