"""
Import data from config file and generate WordPress plugin bootstrap.
"""

import os, sys, argparse, yaml


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

  #write_wp_plugin.create_wordpress_readme()
  #write_wp_plugin.create_skeleton()




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
  
