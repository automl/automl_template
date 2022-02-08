# -*- encoding: utf-8 -*-
from src import (
    package_name,
    author_email,
    description,
    url,
    project_urls,
    version,
)
import setuptools


def read_file(file_name):
    with open(file_name, encoding="utf-8") as fh:
        text = fh.read()
    return text


extras_require = {
    "tests": [
        "pytest>=4.6",
        "pytest-cov",
        "pytest-xdist",
        "pytest-timeout",
        "mypy",
        "isort",
        "black",
        "pydocstyle",
        "pre-commit",
        "flake8",
    ],
    "examples": [
        "matplotlib",
        "jupyter",
        "notebook",
        "seaborn",
    ],
    "docs": [
        "sphinx<4.3",
        "sphinx-gallery",
        "sphinx_bootstrap_theme",
        "numpydoc",
        "sphinx_toolbox",
        "docutils==0.16",
    ],
}


setuptools.setup(
    name=package_name,
    author_email=author_email,
    description=description,
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    url=url,
    project_urls=project_urls,
    version=version,
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    python_requires=">=3.8",
    install_requires=read_file("./requirements.txt").split("\n"),
    extras_require=extras_require,
    test_suite="pytest",
    platforms=["Linux"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering",
    ],
)