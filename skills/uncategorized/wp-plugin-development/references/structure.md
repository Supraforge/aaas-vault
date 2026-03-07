# Plugin Structure

## Recommended Directory Structure

```
plugin-name/
├── assets/
│   ├── css/
│   │   ├── admin.css
│   │   └── public.css
│   ├── js/
│   │   ├── admin.js
│   │   └── public.js
│   └── images/
├── includes/
│   ├── class-plugin-name.php           # Main plugin class
│   ├── class-plugin-name-loader.php    # Hook loader
│   ├── class-plugin-name-activator.php # Activation logic
│   ├── class-plugin-name-deactivator.php
│   ├── class-plugin-name-i18n.php      # Internationalization
│   └── functions.php                    # Helper functions
├── admin/
│   ├── class-plugin-name-admin.php     # Admin functionality
│   ├── views/
│   │   ├── admin-page.php
│   │   └── settings-page.php
│   └── partials/
├── public/
│   ├── class-plugin-name-public.php    # Public functionality
│   ├── views/
│   └── partials/
├── languages/
│   └── plugin-name.pot
├── templates/
│   └── template-parts/
├── vendor/                              # Composer dependencies
├── plugin-name.php                      # Main plugin file
├── uninstall.php                        # Cleanup on uninstall
├── readme.txt                           # WordPress.org readme
├── composer.json
└── package.json
```

## Main Plugin File

### Plugin Header

```php
<?php
/**
 * Plugin Name:       Plugin Name
 * Plugin URI:        https://example.com/plugin
 * Description:       A comprehensive description of the plugin functionality.
 * Version:           1.0.0
 * Requires at least: 6.0
 * Requires PHP:      8.0
 * Author:            Your Agency
 * Author URI:        https://youragency.com
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       plugin-name
 * Domain Path:       /languages
 * Update URI:        https://example.com/plugin-update
 *
 * @package Plugin_Name
 */

// Prevent direct access.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Plugin constants.
define( 'PLUGIN_NAME_VERSION', '1.0.0' );
define( 'PLUGIN_NAME_FILE', __FILE__ );
define( 'PLUGIN_NAME_PATH', plugin_dir_path( __FILE__ ) );
define( 'PLUGIN_NAME_URL', plugin_dir_url( __FILE__ ) );
define( 'PLUGIN_NAME_BASENAME', plugin_basename( __FILE__ ) );

// Autoloader.
require_once PLUGIN_NAME_PATH . 'vendor/autoload.php';

// Plugin activation/deactivation hooks.
register_activation_hook( __FILE__, array( 'Plugin_Name_Activator', 'activate' ) );
register_deactivation_hook( __FILE__, array( 'Plugin_Name_Deactivator', 'deactivate' ) );

// Initialize plugin.
function plugin_name_init() {
    return Plugin_Name::instance();
}
add_action( 'plugins_loaded', 'plugin_name_init' );
```

## Main Plugin Class (Singleton Pattern)

```php
<?php
/**
 * Main plugin class.
 *
 * @package Plugin_Name
 */

class Plugin_Name {

    /**
     * Single instance of the class.
     *
     * @var Plugin_Name
     */
    private static $instance = null;

    /**
     * Plugin loader.
     *
     * @var Plugin_Name_Loader
     */
    protected $loader;

    /**
     * Get single instance.
     *
     * @return Plugin_Name
     */
    public static function instance() {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    /**
     * Constructor.
     */
    private function __construct() {
        $this->load_dependencies();
        $this->set_locale();
        $this->define_admin_hooks();
        $this->define_public_hooks();
        $this->define_rest_api();
        $this->run();
    }

    /**
     * Load dependencies.
     */
    private function load_dependencies() {
        require_once PLUGIN_NAME_PATH . 'includes/class-plugin-name-loader.php';
        require_once PLUGIN_NAME_PATH . 'includes/class-plugin-name-i18n.php';
        require_once PLUGIN_NAME_PATH . 'admin/class-plugin-name-admin.php';
        require_once PLUGIN_NAME_PATH . 'public/class-plugin-name-public.php';

        $this->loader = new Plugin_Name_Loader();
    }

    /**
     * Set locale for internationalization.
     */
    private function set_locale() {
        $i18n = new Plugin_Name_I18n();
        $this->loader->add_action( 'plugins_loaded', $i18n, 'load_plugin_textdomain' );
    }

    /**
     * Register admin hooks.
     */
    private function define_admin_hooks() {
        $admin = new Plugin_Name_Admin();

        // Admin scripts and styles.
        $this->loader->add_action( 'admin_enqueue_scripts', $admin, 'enqueue_styles' );
        $this->loader->add_action( 'admin_enqueue_scripts', $admin, 'enqueue_scripts' );

        // Admin menu.
        $this->loader->add_action( 'admin_menu', $admin, 'add_admin_menu' );

        // Settings.
        $this->loader->add_action( 'admin_init', $admin, 'register_settings' );

        // AJAX handlers.
        $this->loader->add_action( 'wp_ajax_plugin_name_action', $admin, 'ajax_handler' );
    }

    /**
     * Register public hooks.
     */
    private function define_public_hooks() {
        $public = new Plugin_Name_Public();

        $this->loader->add_action( 'wp_enqueue_scripts', $public, 'enqueue_styles' );
        $this->loader->add_action( 'wp_enqueue_scripts', $public, 'enqueue_scripts' );

        // Shortcodes.
        $this->loader->add_action( 'init', $public, 'register_shortcodes' );
    }

    /**
     * Register REST API endpoints.
     */
    private function define_rest_api() {
        $this->loader->add_action( 'rest_api_init', $this, 'register_rest_routes' );
    }

    /**
     * Run the loader.
     */
    public function run() {
        $this->loader->run();
    }
}
```

## Naming Conventions

```php
// Functions: lowercase with underscores, prefixed.
function plugin_name_get_items() {}
function plugin_name_process_data() {}

// Classes: CamelCase with prefix.
class Plugin_Name_Admin {}
class Plugin_Name_REST_Controller {}

// Constants: uppercase with underscores.
define( 'PLUGIN_NAME_VERSION', '1.0.0' );
define( 'PLUGIN_NAME_PATH', __DIR__ );

// Variables: lowercase with underscores.
$user_data = array();
$post_count = 0;

// Hooks: lowercase with underscores, prefixed.
do_action( 'plugin_name_init' );
apply_filters( 'plugin_name_output', $output );
```

## File Headers

```php
<?php
/**
 * Class description.
 *
 * @package    Plugin_Name
 * @subpackage Plugin_Name/Admin
 * @author     Your Name <email@example.com>
 * @since      1.0.0
 */
```
