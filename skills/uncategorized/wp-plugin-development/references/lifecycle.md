# Plugin Lifecycle (Activation/Deactivation/Uninstall)

## Activator Class

```php
<?php
/**
 * Plugin activation handler.
 *
 * @package Plugin_Name
 */

class Plugin_Name_Activator {

    /**
     * Activation hook callback.
     */
    public static function activate() {
        // Check PHP version.
        if ( version_compare( PHP_VERSION, '8.0', '<' ) ) {
            deactivate_plugins( PLUGIN_NAME_BASENAME );
            wp_die(
                esc_html__( 'This plugin requires PHP 8.0 or higher.', 'plugin-name' ),
                'Plugin Activation Error',
                array( 'back_link' => true )
            );
        }

        // Check WordPress version.
        if ( version_compare( get_bloginfo( 'version' ), '6.0', '<' ) ) {
            deactivate_plugins( PLUGIN_NAME_BASENAME );
            wp_die(
                esc_html__( 'This plugin requires WordPress 6.0 or higher.', 'plugin-name' ),
                'Plugin Activation Error',
                array( 'back_link' => true )
            );
        }

        // Create custom database tables.
        self::create_tables();

        // Set default options.
        self::set_default_options();

        // Schedule cron events.
        self::schedule_events();

        // Flush rewrite rules.
        flush_rewrite_rules();

        // Set activation flag for welcome screen.
        set_transient( 'plugin_name_activated', true, 30 );
    }

    /**
     * Create custom database tables.
     */
    private static function create_tables() {
        global $wpdb;

        $charset_collate = $wpdb->get_charset_collate();
        $table_name      = $wpdb->prefix . 'plugin_name_data';

        $sql = "CREATE TABLE IF NOT EXISTS $table_name (
            id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            user_id bigint(20) unsigned NOT NULL,
            title varchar(255) NOT NULL,
            content longtext,
            status varchar(20) DEFAULT 'draft',
            created_at datetime DEFAULT CURRENT_TIMESTAMP,
            updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY user_id (user_id),
            KEY status (status)
        ) $charset_collate;";

        require_once ABSPATH . 'wp-admin/includes/upgrade.php';
        dbDelta( $sql );

        // Store database version.
        update_option( 'plugin_name_db_version', PLUGIN_NAME_VERSION );
    }

    /**
     * Set default plugin options.
     */
    private static function set_default_options() {
        $defaults = array(
            'enabled'       => true,
            'items_per_page' => 10,
            'cache_duration' => 3600,
        );

        if ( false === get_option( 'plugin_name_settings' ) ) {
            add_option( 'plugin_name_settings', $defaults );
        }
    }

    /**
     * Schedule cron events.
     */
    private static function schedule_events() {
        if ( ! wp_next_scheduled( 'plugin_name_daily_cleanup' ) ) {
            wp_schedule_event( time(), 'daily', 'plugin_name_daily_cleanup' );
        }
    }
}
```

## Deactivator Class

```php
<?php
/**
 * Plugin deactivation handler.
 *
 * @package Plugin_Name
 */

class Plugin_Name_Deactivator {

    /**
     * Deactivation hook callback.
     */
    public static function deactivate() {
        // Clear scheduled events.
        $timestamp = wp_next_scheduled( 'plugin_name_daily_cleanup' );
        if ( $timestamp ) {
            wp_unschedule_event( $timestamp, 'plugin_name_daily_cleanup' );
        }

        // Flush rewrite rules.
        flush_rewrite_rules();

        // Clear transients.
        delete_transient( 'plugin_name_cache' );
    }
}
```

## Uninstall (uninstall.php)

```php
<?php
/**
 * Plugin uninstall handler.
 *
 * @package Plugin_Name
 */

// Exit if not uninstalling.
if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
    exit;
}

// Delete options.
delete_option( 'plugin_name_settings' );
delete_option( 'plugin_name_db_version' );

// Delete transients.
delete_transient( 'plugin_name_cache' );

// Delete custom tables.
global $wpdb;
$wpdb->query( "DROP TABLE IF EXISTS {$wpdb->prefix}plugin_name_data" );

// Delete user meta.
delete_metadata( 'user', 0, 'plugin_name_preferences', '', true );

// Delete post meta.
delete_post_meta_by_key( 'plugin_name_meta' );

// Clear any scheduled events.
wp_clear_scheduled_hook( 'plugin_name_daily_cleanup' );

// Clean up any uploaded files.
$upload_dir = wp_upload_dir();
$plugin_dir = $upload_dir['basedir'] . '/plugin-name';
if ( is_dir( $plugin_dir ) ) {
    // Use WP_Filesystem for file operations.
    global $wp_filesystem;
    WP_Filesystem();
    $wp_filesystem->rmdir( $plugin_dir, true );
}
```

## Key Guardrails

1. **Register activation/deactivation at top-level** - Not inside other hooks
2. **Flush rewrite rules carefully** - Only after registering CPTs/rules
3. **Check versions before activation** - PHP and WordPress
4. **Clean up on uninstall** - Options, transients, tables, meta, files
5. **Use `WP_UNINSTALL_PLUGIN` check** - Security guard in uninstall.php
