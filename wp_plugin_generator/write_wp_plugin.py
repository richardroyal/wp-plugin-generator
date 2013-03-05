"""
Import data from config file.
"""

import sys, argparse, yaml



def parse_and_run_command():
  """
  A one-shot function that parses the args, and then runs the command
  that the user specifies on the config file
  """


  config = parse_arguments()
  print config

  #write_wp_plugin.create_wordpress_readme()
  #write_wp_plugin.create_skeleton()









def parse_arguments():
  """
  Loads and checks arguments from STDIN
  """

  # Grab command line arguments
  parser = argparse.ArgumentParser(description='Script that uses a config file to generate a WordPress plugin scaffold.')
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='an integer for the accumulator')
  args = parser.parse_args()
  stream = open( args.infile.name )

  cf = yaml.load(stream)
  
  return cf

