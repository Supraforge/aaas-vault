# WP-Cron Best Practices

## Scheduling Cron Events

```php
// Register custom intervals.
add_filter( 'cron_schedules', function( $schedules ) {
    $schedules['fifteen_minutes'] = array(
        'interval' => 900,
        'display'  => __( 'Every 15 Minutes', 'plugin-name' ),
    );
    return $schedules;
});

// Schedule on activation.
register_activation_hook( __FILE__, function() {
    if ( ! wp_next_scheduled( 'plugin_name_daily_task' ) ) {
        wp_schedule_event( time(), 'daily', 'plugin_name_daily_task' );
    }
});

// Unschedule on deactivation.
register_deactivation_hook( __FILE__, function() {
    wp_clear_scheduled_hook( 'plugin_name_daily_task' );
});
```

## CRITICAL: Avoid Hook Naming Conflicts (Infinite Recursion)

**WARNING:** Never use the same name for a cron hook and an internal action fired within its callback. This causes infinite recursion and fatal errors.

```php
// ❌ FATAL BUG: Infinite recursion!
// Cron hook name matches internal action - WordPress calls do_action('my_cron_hook')
// which triggers the callback, which fires the same action again = infinite loop
wp_schedule_event( time(), 'hourly', 'plugin_name_check_status' );

add_action( 'plugin_name_check_status', 'my_status_check' );

function my_status_check() {
    // This fires the SAME hook that triggered this function!
    do_action( 'plugin_name_check_status' ); // INFINITE LOOP!
}

// ✅ CORRECT: Use different names for cron hook vs internal action
wp_schedule_event( time(), 'hourly', 'plugin_name_check_status' );

add_action( 'plugin_name_check_status', 'my_status_check' );

function my_status_check() {
    // Use a DIFFERENT action name with prefix like 'do_' or '_run'
    do_action( 'plugin_name_do_check_status' ); // Safe - different name
}

// Then other modules can hook to the internal action:
add_action( 'plugin_name_do_check_status', 'actual_status_checker' );
```

## Cron Callback Best Practices

```php
// ✅ GOOD: Add error handling and logging.
add_action( 'plugin_name_daily_cleanup', function() {
    try {
        // Perform cleanup.
        $deleted = plugin_name_cleanup_old_data();

        // Log success.
        if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
            error_log( "Plugin Name: Cleaned up {$deleted} old records" );
        }
    } catch ( Exception $e ) {
        error_log( 'Plugin Name Cron Error: ' . $e->getMessage() );
    }
});

// ✅ GOOD: Prevent long-running cron from timing out.
add_action( 'plugin_name_heavy_task', function() {
    // Increase time limit for long tasks.
    set_time_limit( 300 );

    // Process in batches.
    $batch_size = 100;
    $offset = 0;

    do {
        $items = get_items_batch( $offset, $batch_size );
        foreach ( $items as $item ) {
            process_item( $item );
        }
        $offset += $batch_size;
    } while ( count( $items ) === $batch_size );
});
```

## Audit Checklist for Cron Jobs

When reviewing cron implementations, check:

1. **Hook Name Conflicts** - Ensure cron hook names differ from any `do_action()` calls within callbacks
2. **Proper Scheduling** - Events scheduled on activation, cleared on deactivation
3. **Error Handling** - Callbacks wrapped in try-catch with logging
4. **Batch Processing** - Large data sets processed in chunks
5. **Time Limits** - Long tasks extend execution time
6. **Unique Scheduling** - Check `wp_next_scheduled()` before adding events

## Useful Functions

- `wp_schedule_event( $timestamp, $recurrence, $hook, $args )` - Schedule recurring event
- `wp_schedule_single_event( $timestamp, $hook, $args )` - Schedule one-time event
- `wp_next_scheduled( $hook, $args )` - Get next scheduled time
- `wp_unschedule_event( $timestamp, $hook, $args )` - Unschedule specific event
- `wp_clear_scheduled_hook( $hook, $args )` - Unschedule all events for a hook
- `wp_get_scheduled_event( $hook, $args, $timestamp )` - Get event details
