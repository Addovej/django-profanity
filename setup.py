import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-anti-profanity',
    version='0.0.6',
    packages=find_packages(exclude=('demo', )),
    install_requires=[
        "Django>=2.0",
        "tqdm>=4.32.2",
        "pymorphy2>=0.8"
    ],
    include_package_data=True,
    license='BSD License',
    description="It's a Django app for checking on some profanity words.",
    long_description=README,
    url='',
    author='Artem Verkeev',
    author_email='addovej@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
