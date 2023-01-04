"""Setup configuration for the package."""
# -*- coding: utf-8 -*-
try:
    from setuptools import find_packages, setup
except ImportError:
    import distribute_setup

    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

# pylint: disable=invalid-name
long_desc = """uploader is a markdown and file serve based on cloud storage"""

requires = ["click"]

setup(
    name="uploader",
    version="0.0.1",
    url="https://github.com/lipicoder/uploader",
    license="MIT License",
    author="lipi",
    author_email="lipicoder@qq.com",
    description="uploader is a cli tool for upload image to cloud storage",
    long_description=long_desc,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
