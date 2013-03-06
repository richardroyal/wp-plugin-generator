"""
Create readme.txt file that conforms to WordPress plugin directory
requirements.
@see http://wordpress.org/extend/plugins/about/validator/
"""


def create_readme( config ):
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
  
