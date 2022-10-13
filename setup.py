from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kleopatra_themes/__init__.py
from kleopatra_themes import __version__ as version

setup(
	name="kleopatra_themes",
	version=version,
	description="Kleopatra Themes",
	author="Harpiya Software Technologies",
	author_email="info@harpiya.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
