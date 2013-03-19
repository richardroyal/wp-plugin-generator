"""
Import data from config file and generate WordPress plugin bootstrap.
"""

import os, sys, argparse, yaml, write_wp_readme, write_config_file, write_wp_manifest, write_wp_widgets


def parse_and_run_command():
  """
  A one-shot function that parses the args, and then runs the command
  that the user specifies on the config file.
  """

  config = parse_arguments()
  create_skeleton( config )
  #print "\n\n"
  #print config
  #print "\n\n"
  write_wp_readme.create_readme( config )
  write_wp_manifest.create_manifest( config )
  write_wp_widgets.create_widgets( config )








def parse_arguments():
  """
  Loads and checks arguments from STDIN.
  """
  parser = argparse.ArgumentParser(description='Script that uses a config file to generate a WordPress plugin scaffold.')
  parser.add_argument('-c', '--configure', help='Generate scaffold config.yml to define plugin configuration.', action="store_true")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input configuration file for generating plugin scaffold.')
  args = parser.parse_args()

  
  if args.configure:
    print "Generating config file:  config.yml"
    write_config_file.write_config_yaml()
    sys.exit()
  else:
    print "Generating plugin scaffold: "
    stream = open( args.infile.name )
    cf = yaml.load(stream)
    stream.close()
    print cf['configuration']['folder_name'] + "/"

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
    f = open( cf['folder_name'] + '/lib/functions.php', 'w')
    f = open( cf['folder_name'] + '/admin/functions.php', 'w')
    f = open( cf['folder_name'] + '/lib/db_setup.php', 'w')
    f = open( cf['folder_name'] + '/assets/css/' + cf['folder_name'] + '.css', 'w')
    f = open( cf['folder_name'] + '/assets/js/' + cf['folder_name'] + '.js', 'w')
    f = open( cf['folder_name'] + '/assets/js/' + cf['folder_name'] + '-admin.js', 'w')
    f = open( cf['folder_name'] + '/admin/index.html', 'w')
    f = open( cf['folder_name'] + '/views/index.html', 'w')
    f = open( cf['folder_name'] + '/views/partials/index.html', 'w')
    f = open( cf['folder_name'] + '/lib/index.html', 'w')
    f = open( cf['folder_name'] + '/assets/index.html', 'w')
    f = open( cf['folder_name'] + '/assets/css/index.html', 'w')
    f = open( cf['folder_name'] + '/assets/js/index.html', 'w')
    f = open( cf['folder_name'] + '/assets/images/index.html', 'w')

    for w in config['widgets']:
      f = open( cf['folder_name'] + '/assets/js/' + w['unique_class_name'] + '.js', 'w')
      f = open( cf['folder_name'] + '/assets/js/' + w['unique_class_name'] + '-admin.js', 'w')


  else:
    print "Plugin folder already exists. Exiting."
    sys.exit()


