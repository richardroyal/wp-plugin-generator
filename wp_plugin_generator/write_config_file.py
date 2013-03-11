"""
Functions needed for outputting scaffold config file using:
wp-plugin-generator -c
wp-plugin-generator --configure
Outputs to config.yml
"""

import os, sys, yaml, datetime



def write_config_yaml():
  """
  Write config.yml if it does not exist.
  """
  if not os.path.exists( "config.yml" ):
    f = open("config.yml", 'w')
    f.write(scaffold_config())
    f.close
    
  else:
    print "Config file already exists. Exiting."
    sys.exit()










def scaffold_config():
  s = """
# config.yaml

plugin:
  name: Simple Widget
  uri: http://example.com
  donate_link: http://example.com
  authors: Finn, Jake
  author_emails: you@example.com
  author_uri: http://example.com
  tags: comments, spam
  version: 0.0.1
  requires_at_least: 3.0.1
  tested_up_to: 3.4
  stable_tag: 4.3
  license: GPLv2
  license_url: http://www.gnu.org/licenses/gpl-2.0.html
  short_description: A widget from completing simple tasks.
  long_description:  > 
          A longer description of your plugin.
  installation:  >
          1. Upload the plugin folder to the `/wp-content/plugins/` directory
          2. Activate the plugin through the 'Plugins' menu in WordPress
  frequently_asked_questions:
          - question: A question that someone might have?
            answer: An answer to that question.
          - question: What about foo bar?
            answer: Answer to foo bar dilemma.
  screenshots:
          - description: This screen shot description corresponds to screenshot-1.(png|jpg|jpeg|gif)
          - description: This screen shot description corresponds to screenshot-2.(png|jpg|jpeg|gif)



configuration:
  folder_name: simple_widget
  unique_function_prefix: wpsw_
  unique_constant_prefix: WPSW_



widgets:
 - name: Simple Widget
   unique_class_name: SimpleWidget
   description: A widget that allows simple actions.
   # Attributes
   - name
   - description
   


  """
  return s
