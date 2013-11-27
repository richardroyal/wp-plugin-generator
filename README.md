WordPress Plugin Generator
===================

Script that uses a config file to generate a functioning WordPress plugin scaffolds, with widgets and attributes.


## Basic Usage

Start by generating and filling out the configuration template.

```bash
# Creates config.yml
wp-plugin-generator -c
```

Fill out the template config.yml file which looks like this:

```yml
# config.yml
plugin:
  name: Simple Widget
  tags: comments, spam
  license: GPLv2
  short_description: A widget from completing simple tasks.
  .
  .

configuration:
  folder_name: simple_widget
  unique_prefix: wp_sw
  .
  .
```

Then run the generator on the config file. This will output a plugin template with general and advanced features implemented using the proper WordPress API, including a WordPress plugins directory compatable readme.txt. Comment out or modify what is not needed.

```bash
wp-plugin-generator config.yml
```

## Installation 

Requires `python-yaml`.

```bash
git clone https://github.com/richardroyal/wp-plugin-generator.git
cd wp-plugin-generator

sudo python setup.py install
```

Then just add `wp-plugin-generator` in `bin/` to your PATH.
