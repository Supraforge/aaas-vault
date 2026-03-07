# Settings API

## Admin Class with Settings

```php
<?php
/**
 * Admin functionality.
 *
 * @package Plugin_Name
 */

class Plugin_Name_Admin {

    /**
     * Enqueue admin styles.
     *
     * @param string $hook Current admin page hook.
     */
    public function enqueue_styles( $hook ) {
        // Only load on plugin pages.
        if ( false === strpos( $hook, 'plugin-name' ) ) {
            return;
        }

        wp_enqueue_style(
            'plugin-name-admin',
            PLUGIN_NAME_URL . 'assets/css/admin.css',
            array(),
            PLUGIN_NAME_VERSION
        );
    }

    /**
     * Enqueue admin scripts.
     *
     * @param string $hook Current admin page hook.
     */
    public function enqueue_scripts( $hook ) {
        if ( false === strpos( $hook, 'plugin-name' ) ) {
            return;
        }

        wp_enqueue_script(
            'plugin-name-admin',
            PLUGIN_NAME_URL . 'assets/js/admin.js',
            array( 'jquery' ),
            PLUGIN_NAME_VERSION,
            true
        );

        wp_localize_script(
            'plugin-name-admin',
            'pluginNameAdmin',
            array(
                'ajaxUrl' => admin_url( 'admin-ajax.php' ),
                'nonce'   => wp_create_nonce( 'plugin_name_admin_nonce' ),
                'strings' => array(
                    'confirmDelete' => esc_html__( 'Are you sure?', 'plugin-name' ),
                    'saving'        => esc_html__( 'Saving...', 'plugin-name' ),
                    'saved'         => esc_html__( 'Saved!', 'plugin-name' ),
                ),
            )
        );
    }

    /**
     * Add admin menu pages.
     */
    public function add_admin_menu() {
        // Main menu page.
        add_menu_page(
            esc_html__( 'Plugin Name', 'plugin-name' ),
            esc_html__( 'Plugin Name', 'plugin-name' ),
            'manage_options',
            'plugin-name',
            array( $this, 'render_main_page' ),
            'dashicons-admin-generic',
            30
        );

        // Submenu: Dashboard.
        add_submenu_page(
            'plugin-name',
            esc_html__( 'Dashboard', 'plugin-name' ),
            esc_html__( 'Dashboard', 'plugin-name' ),
            'manage_options',
            'plugin-name',
            array( $this, 'render_main_page' )
        );

        // Submenu: Settings.
        add_submenu_page(
            'plugin-name',
            esc_html__( 'Settings', 'plugin-name' ),
            esc_html__( 'Settings', 'plugin-name' ),
            'manage_options',
            'plugin-name-settings',
            array( $this, 'render_settings_page' )
        );
    }

    /**
     * Register settings.
     */
    public function register_settings() {
        register_setting(
            'plugin_name_settings_group',
            'plugin_name_settings',
            array(
                'type'              => 'array',
                'sanitize_callback' => array( $this, 'sanitize_settings' ),
                'default'           => array(),
            )
        );

        // General Settings Section.
        add_settings_section(
            'plugin_name_general',
            esc_html__( 'General Settings', 'plugin-name' ),
            array( $this, 'render_general_section' ),
            'plugin-name-settings'
        );

        // Enable Feature Field.
        add_settings_field(
            'enabled',
            esc_html__( 'Enable Feature', 'plugin-name' ),
            array( $this, 'render_checkbox_field' ),
            'plugin-name-settings',
            'plugin_name_general',
            array(
                'label_for'   => 'enabled',
                'description' => esc_html__( 'Enable the main feature.', 'plugin-name' ),
            )
        );

        // Items Per Page Field.
        add_settings_field(
            'items_per_page',
            esc_html__( 'Items Per Page', 'plugin-name' ),
            array( $this, 'render_number_field' ),
            'plugin-name-settings',
            'plugin_name_general',
            array(
                'label_for'   => 'items_per_page',
                'min'         => 1,
                'max'         => 100,
                'description' => esc_html__( 'Number of items to display per page.', 'plugin-name' ),
            )
        );
    }

    /**
     * Sanitize settings.
     *
     * @param array $input Raw input.
     * @return array Sanitized input.
     */
    public function sanitize_settings( $input ) {
        $sanitized = array();

        if ( isset( $input['enabled'] ) ) {
            $sanitized['enabled'] = (bool) $input['enabled'];
        }

        if ( isset( $input['items_per_page'] ) ) {
            $sanitized['items_per_page'] = absint( $input['items_per_page'] );
            $sanitized['items_per_page'] = max( 1, min( 100, $sanitized['items_per_page'] ) );
        }

        return $sanitized;
    }

    /**
     * Render checkbox field.
     *
     * @param array $args Field arguments.
     */
    public function render_checkbox_field( $args ) {
        $options = get_option( 'plugin_name_settings' );
        $value   = isset( $options[ $args['label_for'] ] ) ? $options[ $args['label_for'] ] : false;
        ?>
        <input
            type="checkbox"
            id="<?php echo esc_attr( $args['label_for'] ); ?>"
            name="plugin_name_settings[<?php echo esc_attr( $args['label_for'] ); ?>]"
            value="1"
            <?php checked( $value, true ); ?>
        >
        <?php if ( ! empty( $args['description'] ) ) : ?>
            <p class="description"><?php echo esc_html( $args['description'] ); ?></p>
        <?php endif; ?>
        <?php
    }

    /**
     * Render number field.
     *
     * @param array $args Field arguments.
     */
    public function render_number_field( $args ) {
        $options = get_option( 'plugin_name_settings' );
        $value   = isset( $options[ $args['label_for'] ] ) ? $options[ $args['label_for'] ] : '';
        ?>
        <input
            type="number"
            id="<?php echo esc_attr( $args['label_for'] ); ?>"
            name="plugin_name_settings[<?php echo esc_attr( $args['label_for'] ); ?>]"
            value="<?php echo esc_attr( $value ); ?>"
            min="<?php echo esc_attr( $args['min'] ?? '' ); ?>"
            max="<?php echo esc_attr( $args['max'] ?? '' ); ?>"
            class="small-text"
        >
        <?php if ( ! empty( $args['description'] ) ) : ?>
            <p class="description"><?php echo esc_html( $args['description'] ); ?></p>
        <?php endif; ?>
        <?php
    }

    /**
     * Render settings page.
     */
    public function render_settings_page() {
        if ( ! current_user_can( 'manage_options' ) ) {
            return;
        }
        ?>
        <div class="wrap">
            <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>

            <form action="options.php" method="post">
                <?php
                settings_fields( 'plugin_name_settings_group' );
                do_settings_sections( 'plugin-name-settings' );
                submit_button();
                ?>
            </form>
        </div>
        <?php
    }

    /**
     * AJAX handler.
     */
    public function ajax_handler() {
        check_ajax_referer( 'plugin_name_admin_nonce', 'nonce' );

        if ( ! current_user_can( 'manage_options' ) ) {
            wp_send_json_error(
                array( 'message' => esc_html__( 'Unauthorized', 'plugin-name' ) ),
                403
            );
        }

        $action = isset( $_POST['plugin_action'] ) ? sanitize_text_field( wp_unslash( $_POST['plugin_action'] ) ) : '';

        switch ( $action ) {
            case 'save_item':
                $result = $this->save_item( $_POST );
                break;
            case 'delete_item':
                $result = $this->delete_item( $_POST );
                break;
            default:
                wp_send_json_error( array( 'message' => esc_html__( 'Invalid action', 'plugin-name' ) ) );
        }

        if ( is_wp_error( $result ) ) {
            wp_send_json_error( array( 'message' => $result->get_error_message() ) );
        }

        wp_send_json_success( $result );
    }
}
```

## Key Functions

- `register_setting()` - Register the option
- `add_settings_section()` - Add a section to the settings page
- `add_settings_field()` - Add a field to a section
- `settings_fields()` - Output nonce, action, and option_page fields
- `do_settings_sections()` - Render all sections and fields
