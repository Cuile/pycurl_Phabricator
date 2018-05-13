from setuptools import setup, find_packages

setup(
    name="Pycurl_Phabricator",
    packages=['Conduit'],
    version="0.1",

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['pycurl == 7.43.0.1', 'certifi == 2018.1.18', 'sequence2hash'],

    # metadata for upload to PyPI
    author="Cuile",
    author_email="i@cuile.com",
    description="Pycurl based Phabricator API library",
    keywords="phabricator python pycurl",
    # project home page, if any could also include long_description, download_url, classifiers, etc.
    url="https://github.com/Cuile/pycurl_Phabricator"
)
