import sphinx.config
import sphinx.application
import pathlib
import sys
import shutil
import logging
logger = logging.getLogger(__name__)
HERE = pathlib.Path(__file__).absolute().parent
sys.path.append(str(HERE))

import patch  # nopep8

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'VRM'
copyright = '2022, VRMコンソーシアム'
author = 'VRMコンソーシアム'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_sidebars = {
    '**': [
        "sidebar/scroll-start.html",
        'language.html',
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "vrm_topheader.png"
html_favicon = 'favicon.ico'

# sphinx-intl
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
language = "ja"


def setup(app: sphinx.application.Sphinx):
    '''
    https://vrm.dev/licenses/1.0/
    https://vrm.dev/licenses/1.0/en/
    https://vrm.dev/licenses/1.0/pdf/jp.pdf
    https://vrm.dev/licenses/1.0/pdf/en.pdf
    '''

    #
    # markdown の差し替え
    # gettext を使わずに全文差し替えを使うためにビルド前にファイルを入れ替える
    #
    def copy_license_md(app: sphinx.application.Sphinx, config: sphinx.config.Config):
        dst = pathlib.Path(app.confdir) / 'licenses/1.0/index.md'
        if config.language == 'ja':
            src = pathlib.Path(app.confdir).parent / \
                'licenses/ja/1.0/_index.md'
            if src.read_bytes() != dst.read_bytes():
                logger.debug(f'copy {src} to {dst}')
                shutil.copy(src, dst)
        elif config.language == 'en':
            src = pathlib.Path(app.confdir).parent / \
                'licenses/en/1.0/_index.md'
            if src.read_bytes() != dst.read_bytes():
                logger.debug(f'copy {src} to {dst}')
                shutil.copy(src, dst)
        else:
            raise RuntimeError(f'unknown language: {config.language}')

    app.connect('config-inited', copy_license_md, priority=800)