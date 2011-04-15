from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.1'

setup(
    name = 'proxiedssl',
    version = version,
    description = "Django Middleware for handling proxied ssl",
    long_description = open(join(dirname(__file__), 'README')).read() + "\n" + 
                       open(join(dirname(__file__), 'HISTORY')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    keywords = 'django middleware proxy fcgi wsgi ssl',
    author = 'Benjamin Liles',
    author_email = 'benliles@gmail.com',
    url = 'https://github.com/benliles/django-proxiedssl-middleware',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['setuptools']
)
