"""
Import data from config file and generate WordPress plugin bootstrap.
"""

import os, sys, argparse, yaml, datetime


def parse_and_run_command():
  """
  A one-shot function that parses the args, and then runs the command
  that the user specifies on the config file.
  """

  config = parse_arguments()
  create_skeleton( config )
  print "\n\n"
  print config
  print "\n\n"
  create_readme( config )
  create_manifest( config )
  add_plugin_manifest_template( config )








def parse_arguments():
  """
  Loads and checks arguments from STDIN.
  """
  parser = argparse.ArgumentParser(description='Script that uses a config file to generate a WordPress plugin scaffold.')
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='an integer for the accumulator')
  args = parser.parse_args()

  stream = open( args.infile.name )
  cf = yaml.load(stream)
  stream.close()

  return cf


def create_skeleton( config ):
  """
  Create plugin structure in current working folder. Plugin skeleton is template
  used by this utility author in discovering best practices through experience.
  """

  cf = config['configuration']
  if not os.path.exists( cf['folder_name'] ):
    os.makedirs( cf['folder_name'] )
    os.makedirs( cf['folder_name'] + '/admin' )
    os.makedirs( cf['folder_name'] + '/views' )
    os.makedirs( cf['folder_name'] + '/views/partials' )
    os.makedirs( cf['folder_name'] + '/lib' )
    os.makedirs( cf['folder_name'] + '/assets' )
    os.makedirs( cf['folder_name'] + '/assets/css' )
    os.makedirs( cf['folder_name'] + '/assets/js' )
    os.makedirs( cf['folder_name'] + '/assets/images' )

  else:
    print "Plugin folder already exists. Exiting."
    sys.exit()


def create_readme( config ):
  """
  Create readme.txt file that conforms to WordPress plugin directory
  requirements.
  @see http://wordpress.org/extend/plugins/about/validator/
  """
  cf = config['configuration']
  pl = config['plugin']
  f = open(cf['folder_name'] + "/readme.txt", 'w') 
  f.write("=== " + pl['name'] + " ===\n")
  f.write("Donate link: " + pl['donate_link'] + "\n")
  f.write("Tags: " + pl['tags'] + "\n")
  f.write("Requires at least: " + str(pl['requires_at_least']) + "\n")
  f.write("Tested up to: " + str(pl['tested_up_to']) + "\n")
  f.write("Stable tag: " + str(pl['stable_tag']) + "\n")
  f.write("License: " + pl['license'] + "\n")
  f.write("License URI: " + pl['license_url'] + "\n")
  f.write("\n" + pl['short_description'] + "\n\n")

  f.write("== Description ==\n\n")
  f.write(pl['long_description'] + "\n")

  f.write("== Installation ==\n\n")
  f.write(pl['installation'] + "\n")

  f.write("== Frequently Asked Questions ==\n\n")
  for faq in pl['frequently_asked_questions']:
    f.write("= " + faq['question'] + " =\n\n")
    f.write(faq['answer'] + "\n\n")

  f.write("== Screenshots ==\n\n")
  for (i, sh) in enumerate(pl['screenshots']):
    f.write(str(i+1) + ". " + sh['description'] + "\n")

  f.write("\n")

  f.write("== Changelog ==\n\n")
  f.write("= 0.0.1 =\n* Originating Version.\n")

  f.close()
  


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


def add_plugin_manifest_template( config ):
  """
  Write plugin tamplate with standard functions used by most WordPress plugins plugins.
  """
  cf = config['configuration']
  pl = config['plugin']
  f = open(cf['folder_name'] + "/" + cf['folder_name'] + ".php", 'a') 
  f.write("<?php\n")
  f.write("defined('WP_PLUGIN_URL') or die('Restricted access');\n\n")
  f.write("$wpdb;\n")

  f.write("?>")
  f.close()
