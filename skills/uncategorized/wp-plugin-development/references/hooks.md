# Actions and Filters

## Basic Patterns

```php
// ❌ BAD: Hardcoded values, not extensible.
function get_items_per_page() {
    return 10;
}

// ✅ GOOD: Allow filtering.
function get_items_per_page() {
    return apply_filters( 'plugin_name_items_per_page', 10 );
}

// ❌ BAD: No action hooks for extensibility.
function process_order( $order ) {
    save_order( $order );
    send_email( $order );
}

// ✅ GOOD: Add action hooks.
function process_order( $order ) {
    do_action( 'plugin_name_before_process_order', $order );

    save_order( $order );

    do_action( 'plugin_name_order_saved', $order );

    send_email( $order );

    do_action( 'plugin_name_after_process_order', $order );
}

// ✅ GOOD: Filter output before returning.
function get_formatted_price( $price ) {
    $formatted = number_format( $price, 2 );
    return apply_filters( 'plugin_name_formatted_price', $formatted, $price );
}

// ✅ GOOD: Custom hook with multiple parameters.
do_action( 'plugin_name_item_created', $item_id, $item_data, $user_id );

// ✅ GOOD: Filter with default and context.
$title = apply_filters( 'plugin_name_item_title', $title, $item_id, $context );
```

## Hook Loader Pattern

```php
<?php
/**
 * Hook loader class.
 */
class Plugin_Name_Loader {

    /**
     * Registered actions.
     *
     * @var array
     */
    protected $actions = array();

    /**
     * Registered filters.
     *
     * @var array
     */
    protected $filters = array();

    /**
     * Add action.
     */
    public function add_action( $hook, $component, $callback, $priority = 10, $args = 1 ) {
        $this->actions[] = array(
            'hook'      => $hook,
            'component' => $component,
            'callback'  => $callback,
            'priority'  => $priority,
            'args'      => $args,
        );
    }

    /**
     * Add filter.
     */
    public function add_filter( $hook, $component, $callback, $priority = 10, $args = 1 ) {
        $this->filters[] = array(
            'hook'      => $hook,
            'component' => $component,
            'callback'  => $callback,
            'priority'  => $priority,
            'args'      => $args,
        );
    }

    /**
     * Run the loader.
     */
    public function run() {
        foreach ( $this->actions as $action ) {
            add_action(
                $action['hook'],
                array( $action['component'], $action['callback'] ),
                $action['priority'],
                $action['args']
            );
        }

        foreach ( $this->filters as $filter ) {
            add_filter(
                $filter['hook'],
                array( $filter['component'], $filter['callback'] ),
                $filter['priority'],
                $filter['args']
            );
        }
    }
}
```

## Common WordPress Hooks

### Actions
- `init` - After WordPress is loaded
- `admin_init` - Admin area initialization
- `admin_menu` - Add admin menu items
- `admin_enqueue_scripts` - Enqueue admin scripts/styles
- `wp_enqueue_scripts` - Enqueue frontend scripts/styles
- `rest_api_init` - Register REST routes
- `plugins_loaded` - After all plugins loaded
- `wp_ajax_{action}` - AJAX handler for logged-in users
- `wp_ajax_nopriv_{action}` - AJAX handler for logged-out users

### Filters
- `the_content` - Filter post content
- `the_title` - Filter post title
- `cron_schedules` - Add custom cron intervals
- `plugin_action_links_{plugin}` - Add plugin action links
- `admin_body_class` - Add admin body classes
- `body_class` - Add frontend body classes

## Naming Convention

Always prefix hook names with your plugin slug:
```php
// Actions
do_action( 'plugin_name_init' );
do_action( 'plugin_name_before_save' );
do_action( 'plugin_name_after_save' );

// Filters
apply_filters( 'plugin_name_output', $output );
apply_filters( 'plugin_name_settings', $settings );
```
