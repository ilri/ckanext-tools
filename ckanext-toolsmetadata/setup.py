from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-toolsmetadata',
    version=version,
    description="Extension that customize the metadata of a tool",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Carlos Quiros',
    author_email='c.f.quiros@cgiar.org',
    url='https://data.ilri.org/tools',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.toolsmetadata'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        toolsMetadata=ckanext.toolsmetadata.plugin:toolsMetadataPlugin
    ''',
)
