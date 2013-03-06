WordPress Plugin Generator
===================

Script that uses a config file to generate a WordPress plugin scaffold.


## Basic Usage

Start by generating and filling out the configuration template.

```bash
# Creates config.yml
wp-plugin-generator -c
```

Fill out the template config.yml file which looks like this:

```yaml

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
wp-plugin-generator config.yaml
```

