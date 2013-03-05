WordPress Plugin Generator
===================

Script that uses a config file to generate a WordPress plugin scaffold.


## Basic Usage

Start by copying and filling out the configuration template.

```bash

# config.yaml

setup:
      - full_name: Simple Widget
      - short_description: A widget from completing simple tasks.
      - long_description: A longer description....

advanced:
      - unique_prefix: wp_sw

```

Then run the generator on the config file. This will output a plugin template with general and advanced features implemented using the proper WordPress API, including a WordPress plugins directory compatable readme.txt. Comment out or modify what is not needed.

```bash
wp-plugin-generator config.yaml
```

