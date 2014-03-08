from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dgcn.content',
      version=version,
      description="DGCN Content Types",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='TsungWei Hu',
      author_email='',
      url='http://github.com/l34marr/dgcn.content/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dgcn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
