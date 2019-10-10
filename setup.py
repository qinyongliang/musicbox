#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__   ___________________________________________
| \  ||______   |   |______|_____||______|______
|  \_||______   |   |______|     |______||______

________     __________________________  _____ _     _
|  |  ||     ||______  |  |      |_____]|     | \___/
|  |  ||_____|______|__|__|_____ |_____]|_____|_/   \_


+ ------------------------------------------ +
|   NetEase-MusicBox               320kbps   |
+ ------------------------------------------ +
|                                            |
|   ++++++++++++++++++++++++++++++++++++++   |
|   ++++++++++++++++++++++++++++++++++++++   |
|   ++++++++++++++++++++++++++++++++++++++   |
|   ++++++++++++++++++++++++++++++++++++++   |
|   ++++++++++++++++++++++++++++++++++++++   |
|                                            |
|   A sexy cli musicbox based on Python      |
|   Music resource from music.163.com        |
|                                            |
|   Built with love to music by omi          |
|                                            |
+ ------------------------------------------ +

"""
import os
import platform
from setuptools import setup, find_packages
from distutils.command.build_py import build_py

here = os.path.abspath(os.path.dirname(__file__))
about = {}  # type: dict

with open(os.path.join(here, "NEMbox", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    long_description = f.read()

data_files = None
if platform.system() == "Darwin":
    data_files= [("NEMbox", ['NEMbox/osx/HotKey.lib'])]

class OsxHotKeyBuild(build_py):
    def run(self):
        if platform.system() == "Darwin":
            os.system("gcc -fobjc-arc -framework Cocoa -x objective-c -shared -o NEMbox/osx/HotKey.lib NEMbox/osx/hotkey.c")
        build_py.run(self)

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=about["__license__"],
    packages=find_packages(),
    data_files=data_files,
    cmdclass={'build_py': OsxHotKeyBuild},
    install_requires=["requests-cache", "pycryptodomex", "future"],
    entry_points={"console_scripts": ["musicbox = NEMbox.__main__:start"]},
    keywords=["music", "netease", "cli", "player"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Multimedia :: Sound/Audio",
    ],
)
