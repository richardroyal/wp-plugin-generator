try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Script that uses a config file to generate a WordPress plugin scaffold.',
    'author': 'Richard Royal',
    'url': 'https://github.com/richardroyal/wp-plugin-generator',
    'download_url': 'https://github.com/richardroyal/wp-plugin-generator',
    'author_email': '@richardroyal',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wp_plugin_generator'],
    'scripts': [],
    'name': 'wp_plugin_generator'
}

setup(**config)
