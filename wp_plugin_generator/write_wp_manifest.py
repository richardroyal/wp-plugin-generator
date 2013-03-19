"""
Create plugin manifest file will proper WordPress headings.
"""
import os, datetime


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
  f.write("Author URI: " + pl['author_uri'] + "\n")
  f.write("License: " + pl['license'] + "\n")
  f.write("*/\n?>\n")
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
  f.write("?>\n")


def add_plugin_manifest_template(f, config):
  """
  Write plugin tamplate with standard functions used by most WordPress plugins plugins.
  """
  cf = config['configuration']
  pl = config['plugin']
  f.write("<?php\n")
  f.write("defined('WP_PLUGIN_URL') or die('Restricted access');\n\n")
  f.write("global $wpdb;\n")
  
  ucp = cf['unique_constant_prefix']
  f.write("define('" + ucp + "PATH', ABSPATH.PLUGINDIR.'/"+ cf['folder_name']+"/');\n")
  f.write("define('" + ucp + "URL', WP_PLUGIN_URL.'/"+ cf['folder_name']+"/');\n")
  f.write("define('" + ucp + "ROUTE', get_bloginfo('url').'/?"+ cf['unique_function_prefix']+"routing=');\n")
  f.write("require_once(ABSPATH.'wp-admin/includes/upgrade.php');\n")
  f.write('require_once("lib/db_setup.php");\n')
  f.write('require_once("lib/functions.php");\n')
  f.write('require_once("admin/functions.php");\n')
  include_widgets(f, config['widgets'])
  f.write("\n\n\n\n")
  f.write( css_include(config) )
  f.write( js_include(config) )


  f.write("?>")
  f.close()


def include_widgets(f, widgets):

  for w in widgets:
    f.write('require_once("lib/class.' + w['unique_class_name'] + '.php");\n')
    f.write('require_once("views/view.' + w['unique_class_name'] + '.php");\n')
    f.write('require_once("admin/' + w['unique_class_name'] + '/form.' + w['unique_class_name'] + '.php");\n')
  



def css_include(config):
  cf = config['configuration']
  pl = config['plugin']
  fn = cf["folder_name"]
  ufp = cf['unique_function_prefix']
  ucp = cf['unique_constant_prefix']
  s  = "/**\n *  Register and enqueue frontend CSS\n */\n"
  s += "function " + ufp + "stylesheets() {\n"
  s += "  if(!is_admin()){\n"
  s += "    wp_enqueue_style('" + fn + "-style', " + ucp + "URL.'assets/css/" + fn + ".css');\n"
  s += "  }\n"
  s += "}add_action('wp_print_styles', '" + ufp + "stylesheets');\n\n\n"
  
  return s


def js_include(config):
  cf = config['configuration']
  pl = config['plugin']
  fn = cf["folder_name"]
  ufp = cf['unique_function_prefix']
  ucp = cf['unique_constant_prefix']
  s  = "/**\n *  Register and enqueue frontend JavaScript\n */\n"
  s += "function " + ufp + "js() {\n"
  s += "  if(!is_admin()){\n"
  s += "    wp_enqueue_script('jquery');\n"
  s += "    wp_enqueue_script('" + fn + "-js', " + ucp + "URL.'assets/js/" + fn + ".js');\n"
  s += "  }\n"
  s += "}add_action('wp_enqueue_scripts', '" + ufp + "js');\n\n\n"

  s += "/**\n *  Register and enqueue admin JavaScript\n */\n"
  s += "function " + ufp + "admin_js() {\n"
  s += "  wp_enqueue_script('jquery');\n"
  s += "  wp_enqueue_script('" + fn + "-admin-js', " + ucp + "URL.'assets/js/" + fn + "-admin.js');\n"
  s += "}add_action('admin_enqueue_scripts', '" + ufp + "admin_js');\n\n\n"

  return s

