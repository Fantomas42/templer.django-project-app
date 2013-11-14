"""Setup script for templer.django-project-app"""
from setuptools import setup
from setuptools import find_packages

version = '1.2'

setup(
    name='templer.django-project-app',
    version=version,
    description='Templer extension for creating '
    'Django applications within projects.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Code Generators',
    ],
    keywords='templer, django, application',
    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/Fantomas42/templer.django-project-app',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['templer'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'templer.core',
    ],
    entry_points="""
    [paste.paster_create_template]
    django_app = templer.django_project_app:DjangoApp
    django_project_app = templer.django_project_app:DjangoProjectApp

    [templer.templer_structure]
    management_command = templer.django_project_app:ManagementCommandStructure
    """,
)
