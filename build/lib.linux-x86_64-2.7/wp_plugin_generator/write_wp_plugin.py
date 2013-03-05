"""
Import data from config file.
"""

def parse_arguments():
  """
  Loads and checks arguments from STDIN
  """

  # Grab command line arguments
  parser = argparse.ArgumentParser(description='Script that uses a config file to generate a WordPress plugin scaffold.')
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='an integer for the accumulator')
  args = parser.parse_args()
  
 
  stream = open( args.infile.name )
  config = yaml.load(stream)
  
  config['setup']

