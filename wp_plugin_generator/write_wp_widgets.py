"""
Create WordPress widget scaffolds as requested.
"""

import os


def create_widgets( config ):

  for w in config['widgets']:
    fn = config['configuration']['folder_name'] + "/lib/class." + w['unique_class_name'] + ".php"
    f = open(fn, "w")
    f.write( write_widget( config, w ) )
    write_widget_view( config, w )
    write_admin_widget_form( config, w )

    f.close()



def write_widget(config, w):
  """
  Write a single widget using stardard template
  """



  s = """\
<?php
/** 
 *  Adds {0} for widgetized areas.
 *  {2}
 */
class {1} extends WP_Widget{{

  public function __construct() {{
    parent::__construct(
              'ermm_widget', '{0}',
               array( 'description' => "{2}" )
    );

    $this->set_attributes();

  }}


  /**
   * Front-end display of widget.
   *
   * @see WP_Widget::widget()
   *
   * @param array $args     Widget arguments.
   * @param array $instance Saved values from database.
   */
  public function widget( $args, $instance ) {{
    extract( $args );
    $title = apply_filters( 'widget_title', $instance['title'] );

    echo $before_widget;
    if( !empty($title) ) {{
      echo $before_title . $title . $after_title;
    }}
    echo {1}_view( $this );
    echo $after_widget;
  }}


  /**
   * Sanitize widget form values as they are saved.
   *
   * @see WP_Widget::update()
   *
   * @param array $new_instance Values just sent to be saved.
   * @param array $old_instance Previously saved values from database.
   *
   * @return array Updated safe values to be saved.
   */
  public function update( $new_instance, $old_instance ) {{
    $instance = array();

    foreach( $this->attributes as $attr ){{
      $instance[ $attr['name'] ] = strip_tags( $new_instance[ $attr['name'] ] );
    }}

    return $instance;
  }}


  /**
   * Back-end widget form.
   *
   * @see WP_Widget::form()
   *
   * @param array $instance Previously saved values from database.
   */
  public function form( $instance ) {{

    echo {1}_admin_form( $instance, $this );
    
  }}


 /**
  *  Set class attributes into $this->attributes
  *
  *  Set:
  *    array( 'name' => $name, 'type' => $type )
  */
  function set_attributes(){{
    $attributes = array();
    {3}
    $this->attributes = $attributes;
  }}


}}


/* Register Widget */
add_action( 'widgets_init', function(){{
  return register_widget( '{1}' );
}});

?>\n""".format(w['name'], w['unique_class_name'], w['description'], attribute_string(w))

  return s
 




def write_widget_view(config, w):
  """
  Write a file that holds the frontend view on the widget.
  """
  fn = config['configuration']['folder_name'] + "/views/view." + w['unique_class_name'] + ".php"
  f = open(fn, "w")
  
  s = """\
<?php
/**
 *  View for {0} Widget.
 */
function {1}_view($widget){{
  return "WIDGET VIEW {1}";
}}

?>\n""".format(w['name'], w['unique_class_name'], w['description'], w['unique_prefix'])

  f.write(s)
  f.close()




def write_admin_widget_form( config, w ):
  """
  Write a file that holds the admin form for the widget on the widget appearance screen.
  """
  fn = config['configuration']['folder_name'] + "/admin/" + w['unique_class_name']
  os.makedirs( fn )
  fn += "/form." + w['unique_class_name'] + ".php"
  f = open(fn, "w")
  attributes = w['attributes']
#  attr_list = w
  
  s = """\
<?php
/**
 *  View for {0} Widget Admin on appearance screen.
 */
function {1}_admin_form( $instance, $widget ){{


  $s = '';
  foreach( $widget->attributes as $attr ){{
    $s .= {1}_admin_attr_field( $instance, $widget, $attr );
  }}

  return $s;
}}


/**
 *  Function for outputting attribute fields on widget form.
 */
function {1}_admin_attr_field( $instance, $widget, $attr ){{

  $label = $attr['label'];

  if ( isset( $instance[ $attr['name'] ] ) ) {{
    $value = esc_attr( $instance[ $attr['name'] ] );
  }} else {{
    $value = "";
  }}

  if( $attr['type'] == "textarea" ){{

    $s  = '<label for="'.$widget->get_field_id( $attr['name'] ).'">'.$label.'</label>';
    $s .= '<textarea class="widefat" id="'.$widget->get_field_id( $attr['name'] ).'" name="'.$widget->get_field_name( $attr['name'] ).'" rows="16" cols="20">';
    $s .=   $value;
    $s .= '</textarea>';

  }} else {{

    $s  = '<p>';
    $s .= '<label for="'.$widget->get_field_id( $attr['name'] ).'">'.$label.'</label>';
    $s .= '<input class="widefat" id="'.$widget->get_field_id( $attr['name'] ).'" name="'.$widget->get_field_name( $attr['name'] ).'" type="'.$attr['type'].'" value="'.$value.'" />';
    $s .= '</p>';

  }}

  return $s;
}}


?>\n""".format(w['name'], w['unique_class_name'], w['description'])

  f.write(s)
  f.close()




def attribute_string(w):
  """
  Write model attributes from YAML in set_attributes function
  """
  s = ''
  for a in w['attributes']:
    s += "$attributes[] = array('name' => '" + a['name'] + "', 'type' => '" + a['type'] + "', 'label' => '" + a['label'] + "' );\n    " 

  return s


