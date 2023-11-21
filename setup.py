#!/usr/bin/env python

import os
import re
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup  # type: ignore

# TODO: Update the package meta-data
NAME = "streamlit-pydantic"
MAIN_PACKAGE = "streamlit_pydantic"
DESCRIPTION = "Auto-generate Streamlit UI from Pydantic Models & Dataclasses."
URL = "https://github.com/lukasmasuch/streamlit-pydantic"
EMAIL = "lukas.masuch@gmail.com"
AUTHOR = "Lukas Masuch"
LICENSE = "MIT"
REQUIRES_PYTHON = ">=3.7"
VERSION = None  # Only set version if you like to overwrite the version in _about.py

PWD = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with open(os.path.join(PWD, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Extract the version from the _about.py module.
if not VERSION:
    with open(os.path.join(PWD, "src", MAIN_PACKAGE, "_about.py")) as f:  # type: ignore
        VERSION = re.findall(r"__version__\s*=\s*\"(.+)\"", f.read())[0]

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE,
    packages=find_packages(where="src", exclude=("tests", "test", "examples", "docs")),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    zip_safe=False,
    install_requires=["streamlit>=1.14.0", "pydantic>=1.9", "importlib-resources"],
    # deprecated: dependency_links=dependency_links,
    extras_require={
        # extras can be installed via: pip install package[dev]
        "dev": [
            "setuptools",
            "wheel",
            "build",
            "twine",
            "flake8",
            "pytest",
            "pytest-mock",
            "pytest-cov",
            "types-dataclasses",
            "mypy",
            "black",
            "pydocstyle",
            "isort",
            "lazydocs",
            "universal-build",
            "rope",
            "colorama",
        ],
    },
    include_package_data=True,
    package_data={
        # If there are data files included in your packages that need to be
        # 'sample': ['package_data.dat'],
    },
    classifiers=[
        # TODO: Update based on https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": URL + "/releases",
        "Issue Tracker": URL + "/issues",
        "Documentation": URL + "#documentation",
        "Source": URL,
    },
    # entry_points={"console_scripts": [f"{NAME}={MAIN_PACKAGE}._cli:cli"]},
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
)
