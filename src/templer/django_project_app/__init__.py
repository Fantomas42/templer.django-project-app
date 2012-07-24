"""templer.django_project_app"""
import os

from templer.core.vars import StringVar
from templer.core.base import BaseTemplate

HELP_TEXT = """
This creates a basic skeleton for a Django application within a project.
"""

POST_RUN_MESSAGE = """
Now you can install your application into your project by adding these lines.

in %(project_root)s/urls.py:

  url(r'^%(egg)s/', include('%(project_root)s.%(egg)s.urls')),

in %(project_root)s/settings.py:

  INSTALLED_APPS = (
    ...
    '%(project_root)s.%(egg)s',
    ...)
"""

MODEL_VAR = StringVar(
    'model',
    title='Model name',
    description='Default name of the model',
    default='Model',
    help='The name of the Model should be in singular form ' \
    'and in CapitalizedWords format.'
    )


class DjangoProjectApp(BaseTemplate):
    _template_dir = 'templates/django_project_app'
    summary = "A basic Django project application skeleton"
    help = HELP_TEXT
    category = 'Django'
    use_cheetah = True
    vars = [MODEL_VAR]

    def pre(self, command, output_dir, vars):
        super(DjangoProjectApp, self).pre(
            command, output_dir, vars)
        vars['project_root'] = os.path.split(os.getcwd())[-1]
        vars['model_lower'] = vars['model'].lower()

    def post(self, command, output_dir, vars):
        # Don't set the message to self.post_run_msg because the output
        # is really ugly. Simply rename the next assignment to change
        # this behavior.
        self.post_run_message = POST_RUN_MESSAGE % vars
        print self.post_run_message
        super(DjangoProjectApp, self).post(
            command, output_dir, vars)
