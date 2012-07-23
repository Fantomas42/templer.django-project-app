"""templer.django_project_app"""
import os

from templer.core.base import BaseTemplate


class DjangoProjectApp(BaseTemplate):
    _template_dir = 'templates/django_project_app'
    summary = "A basic Django project application skeleton"
    category = 'Django'
    vars = []
    use_cheetah = True
    help = """
This creates a basic skeleton for a Django application within a project.
"""

    def pre(self, command, output_dir, vars):
        vars['project'] = os.path.split(os.getcwd())[-1]
