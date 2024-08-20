from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Python Utily tools'
LONG_DESCRIPTION = 'python common utility tools'

# Setting up
setup(
    name="pyutilities",
    version=VERSION,
    author="PyHashem (Hashem Dalijeh)",
    author_email="<hashemdalijeh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    extras_require={
        'telethon': [
            'telethon',
            'python_socks',
            'async-timeout',
        ],
    },
    keywords=['python', 'telethon', 'telegram', 'tl', 'pyutilities'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)