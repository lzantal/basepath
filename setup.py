from setuptools import setup, find_packages
from basepath import VERSION


# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

setup(
    name = 'basepath',
    version = version,
    description = "Simple base path function to avoid hardcoding file path.",
    long_description = "Use it to create a root base path and call it in your code to return the full path without repeating the parent folder and/or subfolders name. Add more subfolders as needed or new root folder without over writing the original one.",
    author = 'LZAntal',
    author_email = 'LZAntal@gmail.com',
    url = 'https://github.com/lzantal/basepath.git',
    license = '',
    platforms = ['any'],
    packages = find_packages(),
    include_package_data = True,
)
