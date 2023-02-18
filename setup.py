# -*- coding: utf-8 -*-
"""
share-pro
========

Share your computer files to android over wifi.

More details on project's README and
`github page <https://github.com/jakbin/share-pro>`_.


Development Version
-------------------

The share-pro development version can be installed by cloning the git
repository from `github`_::

    git clone git@github.com:jakbin/share-pro.git

.. _github: https://github.com/jakbin/share-pro

License
-------
MIT (see LICENSE file).
"""

from share_pro import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="share-pro",
    version=__version__,
    url="https://github.com/jakbin/share-pro",
    license="MIT License",
    author="jakbin",
    description="Share your computer files to android over wifi.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        ],
    keywords=['share-pro','wifi-file-transfer','file-tranfer'],
    py_modules=['share_pro'],
    entry_points={
        'console_scripts': (
            'share-pro=share_pro:run'
            )
        },
    install_requires=['qrcode','Pillow'],
    zip_safe=False,
    platforms='any'
)
