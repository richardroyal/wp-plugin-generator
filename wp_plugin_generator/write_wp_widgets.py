"""
Create WordPress widget scaffolds as requested.
"""




def create_widgets( config ):

  for w in config['widgets']:
    fn = config['configuration']['folder_name'] + "/lib/class." + w['unique_class_name'] + ".php"
    f = open(fn, "w")
    f.write( write_widget(config, w) )
    write_widget_view(config, w)

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

  public function __construct( ) {{
    parent::__construct(
              'ermm_widget', '{0}',
               array( 'description' => "{2}" )
    );
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
    echo __( 'Hello, World!', 'text_domain' );
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
    $instance['title'] = strip_tags( $new_instance['title'] );

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
    if ( isset( $instance[ 'title' ] ) ) {{
      $title = $instance[ 'title' ];
    }} else {{
      $title = __( 'New title', 'text_domain' );
    }}
    ?>
    <p>
    <label for="<?php echo $this->get_field_id( 'title' ); ?>"><?php _e( 'Title:' ); ?></label> 
    <input class="widefat" id="<?php echo $this->get_field_id( 'title' ); ?>" name="<?php echo $this->get_field_name( 'title' ); ?>" type="text" value="<?php echo esc_attr( $title ); ?>" />
    </p>
    <?php 
  }}


}}


/* Register Widget */
add_action( 'widgets_init', function(){{
  return register_widget( '{1}' );
}});

?>
  """.format(w['name'], w['unique_class_name'], w['description'])

  return s
 




def write_widget_view(config, w):
  """
  Write a file that holds the frontend view on the widget.
  """
  fn = config['configuration']['folder_name'] + "/views/view." + w['unique_class_name'] + ".php"
  f = open(fn, "w")
  
  s = """\
  """

  f.write(s)
  f.close()



