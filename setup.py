from setuptools import setup

setup(
    name = "cfping",
    version = "0.3.1",
    description = "Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    url = "https://github.com/claymation/cfping",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Monitoring',
    ],
    scripts = ['cfping'],
    install_requires = [
        'python-keystoneclient',
        'python-swiftclient',
    ],
)
