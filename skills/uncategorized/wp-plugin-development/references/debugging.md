# Debugging Common Issues

## Activation Hook Not Firing

**Symptoms:**
- Custom tables not created
- Options not set on activation
- Welcome screen not shown

**Common causes:**
1. Hook registered inside another hook (must be at top-level)
2. Wrong main file path in `register_activation_hook()`
3. Plugin is network-activated (uses different hook)
4. PHP fatal error preventing execution

**Fixes:**
```php
// ✅ CORRECT: At top-level in main plugin file
register_activation_hook( __FILE__, array( 'Plugin_Name_Activator', 'activate' ) );

// ❌ WRONG: Inside a hook
add_action( 'plugins_loaded', function() {
    register_activation_hook( __FILE__, 'my_activation' ); // Won't work!
});
```

## Settings Not Saving

**Symptoms:**
- Form submits but values don't persist
- No error messages shown
- Options remain at default values

**Common causes:**
1. Settings not registered with `register_setting()`
2. Wrong option group in `settings_fields()`
3. Missing capability check blocks save
4. Nonce verification failing
5. `sanitize_callback` returning empty

**Debug checklist:**
```php
// 1. Verify settings are registered
register_setting( 'plugin_name_settings_group', 'plugin_name_settings', array(
    'sanitize_callback' => 'my_sanitize_function',
) );

// 2. Verify option group matches
settings_fields( 'plugin_name_settings_group' ); // Must match!

// 3. Check sanitize callback returns data
function my_sanitize_function( $input ) {
    error_log( 'Sanitize input: ' . print_r( $input, true ) );
    // ... sanitize ...
    error_log( 'Sanitize output: ' . print_r( $output, true ) );
    return $output;
}
```

## Security Regressions

**Symptoms:**
- CSRF vulnerabilities
- Unauthorized access to admin functions
- XSS in output

**Common patterns:**
```php
// ❌ Missing nonce
if ( isset( $_POST['save'] ) ) {
    save_data( $_POST );
}

// ❌ Missing capability
function delete_item() {
    $wpdb->delete( $table, array( 'id' => $_POST['id'] ) );
}

// ❌ Missing output escaping
echo $user_input;

// ✅ Correct pattern
if ( isset( $_POST['save'] ) ) {
    // 1. Verify nonce
    if ( ! wp_verify_nonce( $_POST['_wpnonce'], 'save_action' ) ) {
        wp_die( 'Invalid nonce' );
    }

    // 2. Check capability
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( 'Unauthorized' );
    }

    // 3. Sanitize input
    $clean = sanitize_text_field( wp_unslash( $_POST['value'] ) );

    save_data( $clean );
}

// 4. Escape output
echo esc_html( $value );
```

## Cron Infinite Recursion

**Symptoms:**
- Server crashes/timeouts
- Maximum execution time exceeded
- Memory exhaustion

**Cause:** Same name used for cron hook and internal `do_action()`:
```php
// ❌ This causes infinite loop
add_action( 'plugin_name_cron', function() {
    do_action( 'plugin_name_cron' ); // Calls itself!
});
```

**Fix:** Use different names:
```php
// ✅ Use different internal action name
add_action( 'plugin_name_cron', function() {
    do_action( 'plugin_name_do_cron_work' );
});
```

## Debug Mode Settings

Add to `wp-config.php`:
```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
define( 'SCRIPT_DEBUG', true );
define( 'SAVEQUERIES', true );
```

Check debug log at: `wp-content/debug.log`

## Useful Debug Functions

```php
// Log to debug.log
error_log( 'My message' );
error_log( print_r( $array, true ) );

// Dump and die
wp_die( print_r( $data, true ) );

// Check if function exists
if ( function_exists( 'my_function' ) ) { ... }

// Check if class exists
if ( class_exists( 'My_Class' ) ) { ... }

// Check what hooks are attached
global $wp_filter;
error_log( print_r( $wp_filter['init'], true ) );
```

## Query Debugging

```php
// Enable query logging (add to wp-config.php)
define( 'SAVEQUERIES', true );

// View all queries
global $wpdb;
echo '<pre>' . print_r( $wpdb->queries, true ) . '</pre>';

// Show last query
echo $wpdb->last_query;

// Show last error
echo $wpdb->last_error;
```
