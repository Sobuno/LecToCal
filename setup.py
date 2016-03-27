from setuptools import setup, find_packages
from codecs import open

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="lectocal",
    version="1.0.0a1",
    description="Syncronize Lectio schedules to Google Calendar.",
    long_description=long_description,
    url="https://github.com/Hanse00/LecToCal",
    author="Philip Peder Hansen",
    author_email="me@philiphansen.dk",
    license="Apache 2.0",
    classifiers=[
        # Development Status
        "Development Status :: 3 - Alpha",

        # Audience / Topic
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Utilities",

        # Supported Versions
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",

        # Environment Type
        "Environment :: No Input/Output (Daemon)"
    ],
    keywords="lectio google calendar sync utility",
    packages=find_packages(),
    install_requires=[
        "google-api-python-client",
        "requests",
        "lxml",
        "pytz",
        "python-dateutil"
    ],
    entry_points={
        "console_scripts": [
            "lectocal.run=lectocal.run:main",
            "lectocal.gauth=lectocal.gauth:main"
        ]
    }
)
