# Security Best Practices

## Nonce Verification

```php
// ❌ BAD: Missing nonce verification.
if ( isset( $_POST['submit'] ) ) {
    update_option( 'my_option', $_POST['value'] );
}

// ✅ GOOD: Verify nonce.
if ( isset( $_POST['submit'] ) ) {
    if ( ! wp_verify_nonce( $_POST['_wpnonce'], 'plugin_name_save' ) ) {
        wp_die( 'Security check failed' );
    }
    update_option( 'my_option', sanitize_text_field( $_POST['value'] ) );
}
```

## Capability Checks

```php
// ❌ BAD: Missing capability check.
function admin_page_handler() {
    delete_option( 'important_setting' );
}

// ✅ GOOD: Check capabilities.
function admin_page_handler() {
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( 'Unauthorized access' );
    }
    delete_option( 'important_setting' );
}
```

## SQL Injection Prevention

```php
// ❌ BAD: SQL injection vulnerable.
$results = $wpdb->get_results(
    "SELECT * FROM {$wpdb->posts} WHERE post_title = '$title'"
);

// ✅ GOOD: Use prepared statements.
$results = $wpdb->get_results(
    $wpdb->prepare(
        "SELECT * FROM {$wpdb->posts} WHERE post_title = %s",
        $title
    )
);
```

## XSS Prevention (Output Escaping)

```php
// ❌ BAD: XSS vulnerable.
echo $_GET['search'];

// ✅ GOOD: Escape output.
echo esc_html( $_GET['search'] );

// Escaping functions by context:
esc_html( $text );      // HTML content
esc_attr( $value );     // HTML attributes
esc_url( $url );        // URLs
esc_js( $string );      // JavaScript strings
wp_kses_post( $html );  // Allow post HTML tags
```

## Input Sanitization

```php
// Common sanitization functions:
sanitize_text_field( $input );    // Plain text
sanitize_email( $input );         // Email addresses
sanitize_file_name( $input );     // File names
absint( $input );                 // Absolute integer
wp_kses_post( $input );           // HTML with post-allowed tags
sanitize_key( $input );           // Lowercase alphanumeric with dashes/underscores
```

## AJAX Security Pattern

```php
// Register AJAX action
add_action( 'wp_ajax_plugin_name_action', 'plugin_name_ajax_handler' );

function plugin_name_ajax_handler() {
    // 1. Verify nonce
    check_ajax_referer( 'plugin_name_nonce', 'nonce' );

    // 2. Check capability
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_send_json_error( array( 'message' => 'Unauthorized' ), 403 );
    }

    // 3. Sanitize input
    $value = isset( $_POST['value'] )
        ? sanitize_text_field( wp_unslash( $_POST['value'] ) )
        : '';

    // 4. Do the work
    $result = do_something( $value );

    // 5. Return response
    if ( is_wp_error( $result ) ) {
        wp_send_json_error( array( 'message' => $result->get_error_message() ) );
    }

    wp_send_json_success( $result );
}
```

## Security Checklist

- [ ] Input sanitized (`sanitize_*` functions)
- [ ] Output escaped (`esc_*` functions)
- [ ] Nonces verified (`wp_verify_nonce`, `check_ajax_referer`)
- [ ] Capabilities checked (`current_user_can`)
- [ ] Prepared statements used for SQL (`$wpdb->prepare`)
- [ ] Direct file access prevented (`defined( 'ABSPATH' )`)
