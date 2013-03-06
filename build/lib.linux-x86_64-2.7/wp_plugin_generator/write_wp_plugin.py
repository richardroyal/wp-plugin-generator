"""
Import data from config file.
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
  
  return cf



def create_skeleton( config ):
  """
  Create plugin structure in current working folder. Plugin skeleton is template
  used by this utility author in discovering best practices through experience.
  """

  cf = config['configuration'][0]
  pl = config['plugin'][0]
  if not os.path.exists( cf['folder_name'] ):
    os.makedirs( cf['folder_name'] )
    os.makedirs( cf['folder_name'] + '/admin' )
    os.makedirs( cf['folder_name'] + '/views' )
    os.makedirs( cf['folder_name'] + '/lib' )
    os.makedirs( cf['folder_name'] + '/assets' )
    os.makedirs( cf['folder_name'] + '/assets/css' )
    os.makedirs( cf['folder_name'] + '/assets/js' )
    os.makedirs( cf['folder_name'] + '/assets/images' )

  else:
    print "Plugin folder already exists. Exiting."
    sys.exit()



  


