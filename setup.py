#!/usr/bin/env python
import os
from setuptools import setup, find_packages


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("src", "LoadPy", "__init__.py")) as fp:
    exec(fp.read(), version)


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="loadpy",
    version=version['__version__'],
    description="Python package for Downloading Files in a blink of the eye",
    author="Shreyas Bapat",
    author_email="contact@shreyasb.com",
    url="http://shreyasb.com/",
    download_url="https://github.com/JhaPrajjwal/Download-Manager-Python",
    license="MIT",
    keywords=[
        "download", "threads", "idm",
        "download manager", "fast"
    ],
    python_requires=">=3.5",
    install_requires=[
        "numpy",
        "beautifulsoup4>=4.5.3",
        "requests",
    ],
    extras_require={
        'dev': [
            "coverage",
            "pytest-cov",
            "pycodestyle",
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "ipython>=5.0",
            "jupyter-client",
            "ipykernel",
            "ipywidgets",
        ]
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'loadpy = loadpy.cli:main'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software/Engineering",
    ],
    long_description=open('README.md', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
)
