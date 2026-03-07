<?php
/**
 * Plugin Name: Dev Auto Login
 * Description: Auto-login for local development screenshot capture. NEVER use on production.
 * Version: 1.0.0
 *
 * Installation:
 * 1. Copy this file to wp-content/mu-plugins/dev-auto-login.php
 * 2. Use ?dev_login=USER_ID to auto-login as any user
 *
 * Security:
 * - Only works on .local, .test, localhost, or 127.0.0.1 domains
 * - Automatically disabled on production
 * - No credentials stored anywhere
 *
 * Usage:
 * - http://your-site.local/wp-admin/?dev_login=1        (login as user ID 1)
 * - http://your-site.local/wp-admin/?dev_login=admin    (login as username 'admin')
 * - http://your-site.local/?dev_login=5&redirect=/my-dashboard/
 */

// Only run on local development environments
function dev_auto_login_is_local() {
	$host = isset( $_SERVER['HTTP_HOST'] ) ? $_SERVER['HTTP_HOST'] : '';

	// Allowed local domains
	$local_patterns = array(
		'.local',
		'.test',
		'.dev',
		'.localhost',
		'localhost',
		'127.0.0.1',
	);

	foreach ( $local_patterns as $pattern ) {
		if ( false !== strpos( $host, $pattern ) ) {
			return true;
		}
	}

	return false;
}

// Handle auto-login
function dev_auto_login_init() {
	// Safety check - only on local environments
	if ( ! dev_auto_login_is_local() ) {
		return;
	}

	// Check for dev_login parameter
	if ( ! isset( $_GET['dev_login'] ) ) {
		return;
	}

	// Already logged in
	if ( is_user_logged_in() ) {
		// If different user requested, logout first
		$current_user = wp_get_current_user();
		$requested    = sanitize_text_field( $_GET['dev_login'] );

		if ( is_numeric( $requested ) && (int) $current_user->ID === (int) $requested ) {
			return; // Already logged in as requested user
		}
		if ( ! is_numeric( $requested ) && $current_user->user_login === $requested ) {
			return; // Already logged in as requested user
		}

		// Logout to switch users
		wp_logout();
	}

	$user_identifier = sanitize_text_field( $_GET['dev_login'] );
	$user            = null;

	// Find user by ID or username
	if ( is_numeric( $user_identifier ) ) {
		$user = get_user_by( 'id', (int) $user_identifier );
	} else {
		$user = get_user_by( 'login', $user_identifier );
	}

	if ( ! $user ) {
		wp_die(
			sprintf(
				'Dev Auto Login: User "%s" not found. <a href="%s">Go back</a>',
				esc_html( $user_identifier ),
				esc_url( home_url() )
			),
			'User Not Found',
			array( 'response' => 404 )
		);
	}

	// Log in as the user
	wp_set_current_user( $user->ID );
	wp_set_auth_cookie( $user->ID, true );

	// Handle redirect
	$redirect = isset( $_GET['redirect'] ) ? sanitize_text_field( $_GET['redirect'] ) : '';

	if ( $redirect ) {
		wp_safe_redirect( home_url( $redirect ) );
		exit;
	}

	// Redirect to remove the dev_login parameter from URL
	$clean_url = remove_query_arg( array( 'dev_login', 'redirect' ) );
	wp_safe_redirect( $clean_url );
	exit;
}
add_action( 'init', 'dev_auto_login_init', 1 );

// Add admin notice as reminder this is active
function dev_auto_login_admin_notice() {
	if ( ! dev_auto_login_is_local() ) {
		return;
	}
	?>
	<div class="notice notice-info" style="padding: 10px; background: #e7f3fe; border-left-color: #2196F3;">
		<strong>Dev Auto Login Active</strong> -
		Use <code>?dev_login=USER_ID</code> to switch users for testing.
		<a href="<?php echo esc_url( add_query_arg( 'dev_login', '1' ) ); ?>">Switch to Admin</a>
	</div>
	<?php
}
add_action( 'admin_notices', 'dev_auto_login_admin_notice' );
