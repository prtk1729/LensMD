from setuptools import find_packages, setup


__version__ = "0.0.0"

REPO_NAME = "Medical_Image_Analysis"
AUTHOR_USER_NAME = "prtk1729"
SRC_REPO = "Medical_Image_Analysis"
AUTHOR_EMAIL = "prateek.pani4243@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    packages=setuptools.find_packages(),
    install_requires = []
)