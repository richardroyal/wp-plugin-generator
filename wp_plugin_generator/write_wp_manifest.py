"""
Create plugin manifest file will proper WordPress headings.
"""
import datetime


def create_manifest( config ):
  """
  Create plugin manifest file will proper WordPress headings.
  """
  cf = config['configuration']
  pl = config['plugin']
  f = open(cf['folder_name'] + "/" + cf['folder_name'] + ".php", 'w') 
  f.write("<?php\n/*\n")
  f.write("Plugin Name: " + pl['name'] + "\n")
  f.write("Plugin URI: " + pl['uri'] + "\n")
  f.write("Description: " + pl['short_description'] + "\n")
  f.write("Version: " + str(pl['version']) + "\n")
  f.write("Author: " + pl['authors'] + "\n")
  f.write("Author URI: " + pl['name'] + "\n")
  f.write("License: " + pl['name'] + "\n")
  f.write("*/\n?>\n\n")
  write_disclaimer(f, config)
  add_plugin_manifest_template(f, config )
  f.close();


def write_disclaimer(f, config):
  cf = config['configuration']
  pl = config['plugin']
  now = datetime.datetime.now()
  y = str(now.year)
  f.write("<?php\n")
  f.write("/*\n")
  f.write("    Copyright " + y + " " + pl['authors'] + " (" + pl['author_emails'] + ")\n")
  f.write("    This program is distributed in the hope that it will be useful,\n")
  f.write("    but WITHOUT ANY WARRANTY; without even the implied warranty of\n")
  f.write("    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n")
  f.write("*/\n")
  f.write("?>\n\n\n")


def add_plugin_manifest_template(f, config):
  """
  Write plugin tamplate with standard functions used by most WordPress plugins plugins.
  """
  cf = config['configuration']
  pl = config['plugin']
  f.write("<?php\n")
  f.write("defined('WP_PLUGIN_URL') or die('Restricted access');\n\n")
  f.write("$wpdb;\n")

  f.write("?>")
  f.close()
