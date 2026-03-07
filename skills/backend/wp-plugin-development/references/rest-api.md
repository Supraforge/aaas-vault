# REST API Endpoints

## Custom Post Types with REST Support

```php
<?php
/**
 * Register custom post types and taxonomies.
 *
 * @package Plugin_Name
 */

class Plugin_Name_Post_Types {

    /**
     * Register custom post types.
     */
    public function register_post_types() {
        $labels = array(
            'name'                  => _x( 'Projects', 'Post type general name', 'plugin-name' ),
            'singular_name'         => _x( 'Project', 'Post type singular name', 'plugin-name' ),
            'menu_name'             => _x( 'Projects', 'Admin Menu text', 'plugin-name' ),
            'add_new'               => __( 'Add New', 'plugin-name' ),
            'add_new_item'          => __( 'Add New Project', 'plugin-name' ),
            'edit_item'             => __( 'Edit Project', 'plugin-name' ),
            'new_item'              => __( 'New Project', 'plugin-name' ),
            'view_item'             => __( 'View Project', 'plugin-name' ),
            'search_items'          => __( 'Search Projects', 'plugin-name' ),
            'not_found'             => __( 'No projects found.', 'plugin-name' ),
            'not_found_in_trash'    => __( 'No projects found in Trash.', 'plugin-name' ),
        );

        $args = array(
            'labels'              => $labels,
            'public'              => true,
            'publicly_queryable'  => true,
            'show_ui'             => true,
            'show_in_menu'        => true,
            'show_in_rest'        => true, // Enable Gutenberg editor + REST API.
            'rest_base'           => 'projects',
            'menu_position'       => 25,
            'menu_icon'           => 'dashicons-portfolio',
            'capability_type'     => 'post',
            'hierarchical'        => false,
            'supports'            => array(
                'title',
                'editor',
                'author',
                'thumbnail',
                'excerpt',
                'revisions',
            ),
            'has_archive'         => true,
            'rewrite'             => array(
                'slug'       => 'projects',
                'with_front' => false,
            ),
        );

        register_post_type( 'project', $args );
    }

    /**
     * Register custom taxonomies.
     */
    public function register_taxonomies() {
        $args = array(
            'labels'              => array( /* ... */ ),
            'public'              => true,
            'show_in_rest'        => true,
            'rest_base'           => 'project-categories',
            'hierarchical'        => true,
            'rewrite'             => array(
                'slug' => 'project-category',
            ),
        );

        register_taxonomy( 'project_category', array( 'project' ), $args );
    }
}

// Register on init.
add_action( 'init', array( new Plugin_Name_Post_Types(), 'register_post_types' ) );
add_action( 'init', array( new Plugin_Name_Post_Types(), 'register_taxonomies' ) );
```

## Custom REST Routes

```php
<?php
/**
 * REST API functionality.
 *
 * @package Plugin_Name
 */

class Plugin_Name_REST_API {

    /**
     * Namespace.
     *
     * @var string
     */
    protected $namespace = 'plugin-name/v1';

    /**
     * Register routes.
     */
    public function register_routes() {
        // Get/Create items.
        register_rest_route(
            $this->namespace,
            '/items',
            array(
                array(
                    'methods'             => WP_REST_Server::READABLE,
                    'callback'            => array( $this, 'get_items' ),
                    'permission_callback' => array( $this, 'get_items_permissions_check' ),
                    'args'                => $this->get_collection_params(),
                ),
                array(
                    'methods'             => WP_REST_Server::CREATABLE,
                    'callback'            => array( $this, 'create_item' ),
                    'permission_callback' => array( $this, 'create_item_permissions_check' ),
                    'args'                => $this->get_endpoint_args_for_item_schema( WP_REST_Server::CREATABLE ),
                ),
                'schema' => array( $this, 'get_public_item_schema' ),
            )
        );

        // Get/Update/Delete single item.
        register_rest_route(
            $this->namespace,
            '/items/(?P<id>[\d]+)',
            array(
                array(
                    'methods'             => WP_REST_Server::READABLE,
                    'callback'            => array( $this, 'get_item' ),
                    'permission_callback' => array( $this, 'get_item_permissions_check' ),
                ),
                array(
                    'methods'             => WP_REST_Server::EDITABLE,
                    'callback'            => array( $this, 'update_item' ),
                    'permission_callback' => array( $this, 'update_item_permissions_check' ),
                ),
                array(
                    'methods'             => WP_REST_Server::DELETABLE,
                    'callback'            => array( $this, 'delete_item' ),
                    'permission_callback' => array( $this, 'delete_item_permissions_check' ),
                ),
                'schema' => array( $this, 'get_public_item_schema' ),
            )
        );
    }

    /**
     * Check if user can read items.
     *
     * @param WP_REST_Request $request Request object.
     * @return bool|WP_Error
     */
    public function get_items_permissions_check( $request ) {
        return current_user_can( 'read' );
    }

    /**
     * Check if user can create items.
     *
     * @param WP_REST_Request $request Request object.
     * @return bool|WP_Error
     */
    public function create_item_permissions_check( $request ) {
        return current_user_can( 'edit_posts' );
    }

    /**
     * Get items.
     *
     * @param WP_REST_Request $request Request object.
     * @return WP_REST_Response|WP_Error
     */
    public function get_items( $request ) {
        $per_page = $request->get_param( 'per_page' ) ?? 10;
        $page     = $request->get_param( 'page' ) ?? 1;

        global $wpdb;
        $table_name = $wpdb->prefix . 'plugin_name_data';

        $items = $wpdb->get_results(
            $wpdb->prepare(
                "SELECT * FROM $table_name ORDER BY created_at DESC LIMIT %d OFFSET %d",
                $per_page,
                ( $page - 1 ) * $per_page
            )
        );

        $total = $wpdb->get_var( "SELECT COUNT(*) FROM $table_name" );

        $response = rest_ensure_response( $items );
        $response->header( 'X-WP-Total', $total );
        $response->header( 'X-WP-TotalPages', ceil( $total / $per_page ) );

        return $response;
    }

    /**
     * Create item.
     *
     * @param WP_REST_Request $request Request object.
     * @return WP_REST_Response|WP_Error
     */
    public function create_item( $request ) {
        global $wpdb;
        $table_name = $wpdb->prefix . 'plugin_name_data';

        $data = array(
            'user_id' => get_current_user_id(),
            'title'   => sanitize_text_field( $request->get_param( 'title' ) ),
            'content' => wp_kses_post( $request->get_param( 'content' ) ),
            'status'  => sanitize_key( $request->get_param( 'status' ) ?? 'draft' ),
        );

        $result = $wpdb->insert( $table_name, $data, array( '%d', '%s', '%s', '%s' ) );

        if ( false === $result ) {
            return new WP_Error(
                'insert_failed',
                __( 'Failed to create item.', 'plugin-name' ),
                array( 'status' => 500 )
            );
        }

        $item = $wpdb->get_row(
            $wpdb->prepare( "SELECT * FROM $table_name WHERE id = %d", $wpdb->insert_id )
        );

        return rest_ensure_response( $item );
    }

    /**
     * Get item schema.
     *
     * @return array
     */
    public function get_public_item_schema() {
        return array(
            '$schema'    => 'http://json-schema.org/draft-04/schema#',
            'title'      => 'plugin_name_item',
            'type'       => 'object',
            'properties' => array(
                'id'         => array(
                    'description' => __( 'Unique identifier for the item.', 'plugin-name' ),
                    'type'        => 'integer',
                    'readonly'    => true,
                ),
                'title'      => array(
                    'description' => __( 'The title for the item.', 'plugin-name' ),
                    'type'        => 'string',
                    'required'    => true,
                ),
                'content'    => array(
                    'description' => __( 'The content for the item.', 'plugin-name' ),
                    'type'        => 'string',
                ),
                'status'     => array(
                    'description' => __( 'The status for the item.', 'plugin-name' ),
                    'type'        => 'string',
                    'enum'        => array( 'draft', 'published', 'archived' ),
                    'default'     => 'draft',
                ),
            ),
        );
    }
}
```

## Key Patterns

1. **Always provide `permission_callback`** - Required since WP 5.5
2. **Use `WP_REST_Server` constants** - `READABLE`, `CREATABLE`, `EDITABLE`, `DELETABLE`
3. **Sanitize input** - Use `sanitize_*` functions
4. **Prepared statements** - Use `$wpdb->prepare()` for queries
5. **Provide schema** - Enables validation and documentation
6. **Set pagination headers** - `X-WP-Total` and `X-WP-TotalPages`
