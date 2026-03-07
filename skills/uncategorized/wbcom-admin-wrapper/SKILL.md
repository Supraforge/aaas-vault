---
name: wbcom-admin-wrapper
description: >-
  Standardized WordPress admin UI framework used across all Wbcom Designs
  plugins. Provides consistent styling, settings pages, license integration, and
  plugin management.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Wbcom Admin Wrapper

Standardized WordPress admin UI framework used across all Wbcom Designs plugins. Provides consistent styling, settings pages, license integration, and plugin management.

## When to Use

Use this skill when:
- Creating a new Wbcom Designs plugin (free or pro)
- Adding admin settings pages to a plugin
- Integrating EDD license management for Pro plugins
- Ensuring UI consistency across plugin family

## Directory Structure

```
your-plugin/
├── admin/
│   └── wbcom/
│       ├── wbcom-admin-settings.php      # Core admin class
│       ├── wbcom-paid-plugin-settings.php # License page (Pro only)
│       ├── assets/
│       │   ├── css/
│       │   │   └── wbcom-admin-setting.css
│       │   └── js/
│       │       └── wbcom-admin-setting.js
│       └── templates/
│           ├── wbcom-license-page.php     # License page template
│           ├── wbcomplugins.php           # Plugin management
│           ├── wbcom-themes-page.php      # Themes showcase
│           └── wbcom-support.php          # Support page
├── edd-license/                           # Pro plugins only
│   ├── edd-plugin-license.php            # License handler
│   └── EDD_{PREFIX}_Plugin_Updater.php   # Updater class
└── your-plugin.php
```

## CSS Custom Properties

The wrapper uses CSS variables for consistent theming:

```css
:root {
    /* Primary Colors */
    --primary-color: #2A32EF;
    --secondary-color: #272B41;
    --success-color: #4fb845;
    --error-color: #FF0000;

    /* Backgrounds */
    --background-light: #F6F7FE;
    --background-lighter: #FBFBFB;
    --background-input: #F4F5F7;

    /* Borders */
    --border-color: rgba(200, 197, 218, 0.30);
    --border-color-medium: rgba(200, 197, 218, 0.50);

    /* Typography */
    --text-dark: #1d2327;
    --text-medium: #4c5261;
    --text-light: #646F89;

    /* Spacing */
    --spacing-xs: 8px;
    --spacing-sm: 12px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;

    /* Border Radius */
    --border-radius-sm: 4px;
    --border-radius-md: 8px;
    --border-radius-lg: 12px;
}
```

## HTML Structure Patterns

### Settings Page Layout

```php
<div class="wbcom-tab-content">
    <div class="wbcom-wrapper-admin">
        <!-- Title Section -->
        <div class="wbcom-admin-title-section">
            <h3><?php esc_html_e( 'Section Title', 'your-text-domain' ); ?></h3>
        </div>

        <!-- Options Container -->
        <div class="wbcom-admin-option-wrap wbcom-admin-option-wrap-view">
            <form method="post" action="options.php">
                <?php settings_fields( 'your_settings_group' ); ?>

                <!-- Individual Setting Row -->
                <div class="wbcom-settings-section-wrap">
                    <div class="wbcom-settings-section-options-heading">
                        <label for="setting_id">
                            <?php esc_html_e( 'Setting Label', 'your-text-domain' ); ?>
                        </label>
                        <p class="description">
                            <?php esc_html_e( 'Setting description here.', 'your-text-domain' ); ?>
                        </p>
                    </div>
                    <div class="wbcom-settings-section-options">
                        <!-- Input control here -->
                    </div>
                </div>

                <!-- Submit Button -->
                <div class="wbcom-settings-section-wrap">
                    <?php submit_button(); ?>
                </div>
            </form>
        </div>
    </div>
</div>
```

### Toggle Switch

```php
<div class="wbcom-settings-section-options">
    <div class="wb-admin-switch">
        <input type="hidden" name="option_name" value="no" />
        <input
            type="checkbox"
            id="option_id"
            name="option_name"
            value="yes"
            <?php checked( 'yes', get_option( 'option_name' ) ); ?>
        />
        <label for="option_id"></label>
    </div>
</div>
```

### Radio Button Group

```php
<div class="wbcom-settings-section-options">
    <label class="wbcom-radio-option">
        <input type="radio" name="option_name" value="value1"
            <?php checked( 'value1', get_option( 'option_name', 'value1' ) ); ?> />
        <?php esc_html_e( 'Option 1', 'your-text-domain' ); ?>
    </label>
    <label class="wbcom-radio-option">
        <input type="radio" name="option_name" value="value2"
            <?php checked( 'value2', get_option( 'option_name' ) ); ?> />
        <?php esc_html_e( 'Option 2', 'your-text-domain' ); ?>
    </label>
</div>
```

### Select Dropdown

```php
<div class="wbcom-settings-section-options">
    <select name="option_name" id="option_id">
        <option value="val1" <?php selected( 'val1', get_option( 'option_name' ) ); ?>>
            <?php esc_html_e( 'Value 1', 'your-text-domain' ); ?>
        </option>
        <option value="val2" <?php selected( 'val2', get_option( 'option_name' ) ); ?>>
            <?php esc_html_e( 'Value 2', 'your-text-domain' ); ?>
        </option>
    </select>
</div>
```

### Grid Layout (2 Columns)

```php
<div class="wbcom-settings-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
    <label class="wbcom-checkbox-option">
        <input type="checkbox" name="options[]" value="item1" />
        <?php esc_html_e( 'Item 1', 'your-text-domain' ); ?>
    </label>
    <label class="wbcom-checkbox-option">
        <input type="checkbox" name="options[]" value="item2" />
        <?php esc_html_e( 'Item 2', 'your-text-domain' ); ?>
    </label>
</div>
```

### Grid Layout (3 Columns)

```php
<div class="wbcom-settings-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
    <!-- Items here -->
</div>
```

## Tab System

### Registering Tabs

```php
// In your admin class constructor
add_filter( 'yourplugin_admin_tabs', array( $this, 'register_tabs' ) );

public function register_tabs( $tabs ) {
    $tabs['general']  = __( 'General', 'your-text-domain' );
    $tabs['settings'] = __( 'Settings', 'your-text-domain' );
    $tabs['pro']      = __( 'Pro Features', 'your-text-domain' );
    return $tabs;
}
```

### Tab Navigation CSS Classes

```css
/* Tab wrapper */
.wbcom-tabs-section-container .wbcom-nav-tabs {}

/* Individual tab */
.wbcom-tabs-section-container .wbcom-nav-tab {}

/* Active tab */
.wbcom-tabs-section-container .wbcom-nav-tab.is_active {}

/* Tab icon */
.wbcom-nav-tab-icon-general::before { content: "\f107"; }
.wbcom-nav-tab-icon-settings::before { content: "\f111"; }
```

### Tab Content Template

Create `admin/tab-templates/your-setting-{tab-slug}-tab.php`:

```php
<?php
/**
 * Tab content template.
 *
 * @package Your_Plugin
 */

defined( 'ABSPATH' ) || exit;
?>
<div class="wbcom-tab-content">
    <!-- Tab content here using patterns above -->
</div>
```

## EDD License Integration (Pro Plugins)

### Step 1: Define Constants

In your main plugin file:

```php
// Plugin constants
define( 'YOUR_PLUGIN_VERSION', '1.0.0' );
define( 'YOUR_PLUGIN_FILE', __FILE__ );
define( 'YOUR_PLUGIN_PATH', plugin_dir_path( __FILE__ ) );

// Include license handler
require_once YOUR_PLUGIN_PATH . 'edd-license/edd-plugin-license.php';
```

### Step 2: Create License Handler

Create `edd-license/edd-plugin-license.php`:

```php
<?php
/**
 * EDD License Handler.
 *
 * @package Your_Plugin_Pro
 */

defined( 'ABSPATH' ) || exit;

// Store URL - your EDD store.
define( 'EDD_YOUR_PLUGIN_STORE_URL', 'https://wbcomdesigns.com/' );

// Product name - must match EDD download name exactly.
define( 'EDD_YOUR_PLUGIN_ITEM_NAME', 'Your Plugin Pro' );

// License page slug.
define( 'EDD_YOUR_PLUGIN_LICENSE_PAGE', 'wbcom-license-page' );

// Load the updater class.
if ( ! class_exists( 'EDD_YOUR_PLUGIN_Plugin_Updater' ) ) {
    include dirname( __FILE__ ) . '/EDD_YOUR_PLUGIN_Plugin_Updater.php';
}

/**
 * Initialize the updater.
 */
function edd_your_plugin_updater() {
    $license_key = trim( get_option( 'edd_wbcom_your_plugin_license_key' ) );

    $edd_updater = new EDD_YOUR_PLUGIN_Plugin_Updater(
        EDD_YOUR_PLUGIN_STORE_URL,
        YOUR_PLUGIN_FILE,
        array(
            'version'   => YOUR_PLUGIN_VERSION,
            'license'   => $license_key,
            'item_name' => EDD_YOUR_PLUGIN_ITEM_NAME,
            'author'    => 'wbcomdesigns',
            'url'       => home_url(),
        )
    );
}
add_action( 'admin_init', 'edd_your_plugin_updater', 0 );

/**
 * Register license option.
 */
function edd_wbcom_your_plugin_register_option() {
    register_setting(
        'edd_wbcom_your_plugin_license',
        'edd_wbcom_your_plugin_license_key',
        'edd_your_plugin_sanitize_license'
    );
}
add_action( 'admin_init', 'edd_wbcom_your_plugin_register_option' );

/**
 * Sanitize license input.
 */
function edd_your_plugin_sanitize_license( $new ) {
    $old = get_option( 'edd_wbcom_your_plugin_license_key' );
    if ( $old && $old !== $new ) {
        delete_option( 'edd_wbcom_your_plugin_license_status' );
    }
    return sanitize_text_field( $new );
}

/**
 * Activate license.
 */
function edd_wbcom_your_plugin_activate_license() {
    if ( ! isset( $_POST['edd_your_plugin_license_activate'] ) ) {
        return;
    }

    if ( ! check_admin_referer( 'edd_wbcom_your_plugin_nonce', 'edd_wbcom_your_plugin_nonce' ) ) {
        return;
    }

    $license = isset( $_POST['edd_wbcom_your_plugin_license_key'] )
        ? sanitize_text_field( wp_unslash( $_POST['edd_wbcom_your_plugin_license_key'] ) )
        : '';

    $api_params = array(
        'edd_action' => 'activate_license',
        'license'    => $license,
        'item_name'  => rawurlencode( EDD_YOUR_PLUGIN_ITEM_NAME ),
        'url'        => home_url(),
    );

    $response = wp_remote_post(
        EDD_YOUR_PLUGIN_STORE_URL,
        array(
            'timeout'   => 15,
            'sslverify' => true,
            'body'      => $api_params,
        )
    );

    if ( is_wp_error( $response ) || 200 !== wp_remote_retrieve_response_code( $response ) ) {
        $message = is_wp_error( $response )
            ? $response->get_error_message()
            : __( 'An error occurred, please try again.', 'your-text-domain' );
    } else {
        $license_data = json_decode( wp_remote_retrieve_body( $response ) );

        if ( false === $license_data->success ) {
            switch ( $license_data->error ) {
                case 'expired':
                    $message = sprintf(
                        __( 'Your license key expired on %s.', 'your-text-domain' ),
                        date_i18n( get_option( 'date_format' ), strtotime( $license_data->expires, time() ) )
                    );
                    break;
                case 'disabled':
                case 'revoked':
                    $message = __( 'Your license key has been disabled.', 'your-text-domain' );
                    break;
                case 'missing':
                    $message = __( 'Invalid license.', 'your-text-domain' );
                    break;
                case 'invalid':
                case 'site_inactive':
                    $message = __( 'Your license is not active for this URL.', 'your-text-domain' );
                    break;
                case 'item_name_mismatch':
                    $message = sprintf(
                        __( 'This appears to be an invalid license key for %s.', 'your-text-domain' ),
                        EDD_YOUR_PLUGIN_ITEM_NAME
                    );
                    break;
                case 'no_activations_left':
                    $message = __( 'Your license key has reached its activation limit.', 'your-text-domain' );
                    break;
                default:
                    $message = __( 'An error occurred, please try again.', 'your-text-domain' );
                    break;
            }
        }
    }

    if ( ! empty( $message ) ) {
        $redirect = add_query_arg(
            array(
                'page'          => EDD_YOUR_PLUGIN_LICENSE_PAGE,
                'sl_activation' => 'false',
                'message'       => rawurlencode( $message ),
            ),
            admin_url( 'admin.php' )
        );
        wp_safe_redirect( $redirect );
        exit;
    }

    update_option( 'edd_wbcom_your_plugin_license_key', $license );
    update_option( 'edd_wbcom_your_plugin_license_status', $license_data->license );

    if ( isset( $license_data->expires ) ) {
        update_option( 'edd_wbcom_your_plugin_license_expiry', strtotime( $license_data->expires ) );
    }

    wp_safe_redirect( admin_url( 'admin.php?page=' . EDD_YOUR_PLUGIN_LICENSE_PAGE ) );
    exit;
}
add_action( 'admin_init', 'edd_wbcom_your_plugin_activate_license' );

/**
 * Deactivate license.
 */
function edd_wbcom_your_plugin_deactivate_license() {
    if ( ! isset( $_POST['edd_your_plugin_license_deactivate'] ) ) {
        return;
    }

    if ( ! check_admin_referer( 'edd_wbcom_your_plugin_nonce', 'edd_wbcom_your_plugin_nonce' ) ) {
        return;
    }

    $license = trim( get_option( 'edd_wbcom_your_plugin_license_key' ) );

    $api_params = array(
        'edd_action' => 'deactivate_license',
        'license'    => $license,
        'item_name'  => rawurlencode( EDD_YOUR_PLUGIN_ITEM_NAME ),
        'url'        => home_url(),
    );

    $response = wp_remote_post(
        EDD_YOUR_PLUGIN_STORE_URL,
        array(
            'timeout'   => 15,
            'sslverify' => true,
            'body'      => $api_params,
        )
    );

    if ( is_wp_error( $response ) || 200 !== wp_remote_retrieve_response_code( $response ) ) {
        $message = is_wp_error( $response )
            ? $response->get_error_message()
            : __( 'An error occurred, please try again.', 'your-text-domain' );
        $redirect = add_query_arg(
            array(
                'page'          => EDD_YOUR_PLUGIN_LICENSE_PAGE,
                'sl_activation' => 'false',
                'message'       => rawurlencode( $message ),
            ),
            admin_url( 'admin.php' )
        );
        wp_safe_redirect( $redirect );
        exit;
    }

    $license_data = json_decode( wp_remote_retrieve_body( $response ) );

    if ( 'deactivated' === $license_data->license ) {
        delete_option( 'edd_wbcom_your_plugin_license_status' );
        delete_option( 'edd_wbcom_your_plugin_license_expiry' );
    }

    wp_safe_redirect( admin_url( 'admin.php?page=' . EDD_YOUR_PLUGIN_LICENSE_PAGE ) );
    exit;
}
add_action( 'admin_init', 'edd_wbcom_your_plugin_deactivate_license' );

/**
 * Render license section on Wbcom license page.
 */
function wbcom_your_plugin_render_license_section() {
    $license = get_option( 'edd_wbcom_your_plugin_license_key', '' );
    $status  = get_option( 'edd_wbcom_your_plugin_license_status' );

    $plugin_data = get_plugin_data( YOUR_PLUGIN_FILE, true, true );

    if ( 'valid' === $status ) {
        $status_class = 'active';
        $status_text  = __( 'Active', 'your-text-domain' );
    } elseif ( 'expired' === $status ) {
        $status_class = 'expired';
        $status_text  = __( 'Expired', 'your-text-domain' );
    } else {
        $status_class = 'inactive';
        $status_text  = __( 'Inactive', 'your-text-domain' );
    }
    ?>
    <table class="form-table wb-license-form-table mobile-license-headings">
        <thead>
            <tr>
                <th class="wb-product-th"><?php esc_html_e( 'Product', 'your-text-domain' ); ?></th>
                <th class="wb-version-th"><?php esc_html_e( 'Version', 'your-text-domain' ); ?></th>
                <th class="wb-key-th"><?php esc_html_e( 'Key', 'your-text-domain' ); ?></th>
                <th class="wb-status-th"><?php esc_html_e( 'Status', 'your-text-domain' ); ?></th>
                <th class="wb-action-th"><?php esc_html_e( 'Action', 'your-text-domain' ); ?></th>
                <th></th>
            </tr>
        </thead>
    </table>
    <form method="post" action="options.php">
        <?php settings_fields( 'edd_wbcom_your_plugin_license' ); ?>
        <table class="form-table wb-license-form-table">
            <tr>
                <td class="wb-plugin-name"><?php echo esc_html( $plugin_data['Name'] ); ?></td>
                <td class="wb-plugin-version"><?php echo esc_html( $plugin_data['Version'] ); ?></td>
                <td class="wb-plugin-license-key">
                    <input id="edd_wbcom_your_plugin_license_key"
                           name="edd_wbcom_your_plugin_license_key"
                           type="text"
                           class="regular-text"
                           value="<?php echo esc_attr( $license ); ?>" />
                </td>
                <td class="wb-license-status <?php echo esc_attr( $status_class ); ?>">
                    <?php echo esc_html( $status_text ); ?>
                </td>
                <td class="wb-license-action">
                    <?php wp_nonce_field( 'edd_wbcom_your_plugin_nonce', 'edd_wbcom_your_plugin_nonce' ); ?>
                    <?php if ( 'active' === $status_class ) : ?>
                        <input type="submit"
                               class="button-secondary"
                               name="edd_your_plugin_license_deactivate"
                               value="<?php esc_attr_e( 'Deactivate License', 'your-text-domain' ); ?>"/>
                    <?php else : ?>
                        <input type="submit"
                               class="button-secondary"
                               name="edd_your_plugin_license_activate"
                               value="<?php esc_attr_e( 'Activate License', 'your-text-domain' ); ?>"/>
                    <?php endif; ?>
                </td>
            </tr>
        </table>
    </form>
    <?php
}
add_action( 'wbcom_add_plugin_license_code', 'wbcom_your_plugin_render_license_section' );
```

### Step 3: Create License Page Class

Create `admin/wbcom/wbcom-paid-plugin-settings.php`:

```php
<?php
/**
 * Class to add license page for paid plugin.
 *
 * @package Your_Plugin_Pro
 */

defined( 'ABSPATH' ) || exit;

if ( ! class_exists( 'Wbcom_Paid_Plugin_Settings' ) ) {

    class Wbcom_Paid_Plugin_Settings {

        public function __construct() {
            add_action( 'admin_menu', array( $this, 'wbcom_admin_license_page' ), 999 );
            add_action( 'wbcom_add_header_menu', array( $this, 'wbcom_add_header_license_menu' ) );
        }

        public function wbcom_admin_license_page() {
            add_submenu_page(
                'wbcomplugins',
                esc_html__( 'License', 'your-text-domain' ),
                esc_html__( 'License', 'your-text-domain' ),
                'manage_options',
                'wbcom-license-page',
                array( $this, 'wbcom_license_submenu_page_callback' )
            );
        }

        public function wbcom_license_submenu_page_callback() {
            include YOUR_PLUGIN_PATH . 'admin/wbcom/templates/wbcom-license-page.php';
        }

        public function wbcom_add_header_license_menu() {
            $page = isset( $_GET['page'] ) ? sanitize_text_field( wp_unslash( $_GET['page'] ) ) : '';
            $license_page_active = 'wbcom-license-page' === $page ? 'is_active' : '';
            ?>
            <li class="wb_admin_nav_item <?php echo esc_attr( $license_page_active ); ?>">
                <a href="<?php echo esc_url( admin_url( 'admin.php?page=wbcom-license-page' ) ); ?>">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 22H4C3.44772 22 3 21.5523 3 21V3C3 2.44772 3.44772 2 4 2H20C20.5523 2 21 2.44772 21 3V21C21 21.5523 20.5523 22 20 22ZM19 20V4H5V20H19ZM7 6H11V10H7V6ZM7 12H17V14H7V12ZM7 16H17V18H7V16ZM13 7H17V9H13V7Z"></path>
                    </svg>
                    <h4><?php esc_html_e( 'License', 'your-text-domain' ); ?></h4>
                </a>
            </li>
            <?php
        }
    }

    new Wbcom_Paid_Plugin_Settings();
}
```

### Step 4: Copy the Updater Class

Copy `EDD_{PREFIX}_Plugin_Updater.php` from an existing plugin and update:
- Class name: `EDD_YOUR_PLUGIN_Plugin_Updater`
- Filter name: `edd_yourplugin_sl_api_request_verify_ssl`

## Key Hooks

### Actions

| Hook | Purpose | Example |
|------|---------|---------|
| `wbcom_add_plugin_license_code` | Render license row on license page | License table row |
| `wbcom_add_header_menu` | Add item to header navigation | License menu item |
| `yourplugin_admin_settings_{tab}_content` | Render tab content | Tab-specific settings |

### Filters

| Filter | Purpose | Example |
|--------|---------|---------|
| `yourplugin_admin_tabs` | Register admin tabs | Add new tabs |

## Option Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| License Key | `edd_wbcom_{plugin}_license_key` | `edd_wbcom_bupr_pro_license_key` |
| License Status | `edd_wbcom_{plugin}_license_status` | `edd_wbcom_bupr_pro_license_status` |
| License Expiry | `edd_wbcom_{plugin}_license_expiry` | `edd_wbcom_bupr_pro_license_expiry` |
| Plugin Settings | `{plugin}_{setting}` | `bupr_enable_flagging` |

## File Templates Location

Templates from existing plugins:

```
wp-content/plugins/buddypress-member-review/admin/wbcom/
├── wbcom-admin-settings.php        # Core wrapper
├── assets/css/wbcom-admin-setting.css  # Full CSS
└── templates/
    ├── wbcom-license-page.php      # License page
    └── wbcomplugins.php            # Plugin management

wp-content/plugins/buddypress-member-review-pro/
├── edd-license/
│   ├── edd-plugin-license.php      # License handler
│   └── EDD_BUPR_PRO_Plugin_Updater.php  # Updater
└── admin/wbcom/
    └── wbcom-paid-plugin-settings.php  # License page menu
```

## CSS Class Reference

### Layout Classes

| Class | Purpose |
|-------|---------|
| `.wbcom-tab-content` | Tab content wrapper |
| `.wbcom-wrapper-admin` | Main admin wrapper |
| `.wbcom-admin-title-section` | Section title |
| `.wbcom-admin-option-wrap` | Options container |
| `.wbcom-settings-section-wrap` | Individual setting row |
| `.wbcom-settings-section-options-heading` | Setting label/description |
| `.wbcom-settings-section-options` | Setting input control |

### Form Element Classes

| Class | Purpose |
|-------|---------|
| `.wb-admin-switch` | Toggle switch container |
| `.wbcom-radio-option` | Radio button label |
| `.wbcom-checkbox-option` | Checkbox label |
| `.wbcom-settings-grid` | Grid layout container |

### License Page Classes

| Class | Purpose |
|-------|---------|
| `.wb-license-form-table` | License table |
| `.wb-plugin-name` | Product name cell |
| `.wb-plugin-version` | Version cell |
| `.wb-plugin-license-key` | License key input cell |
| `.wb-license-status` | Status indicator cell |
| `.wb-license-action` | Action button cell |
| `.active` / `.inactive` / `.expired` | Status modifiers |

## Pro Plugin Architecture

### Feature Gate Pattern

```php
class Your_Plugin_Pro_Features {

    /**
     * Check if Pro plugin is active (not license - features always work).
     */
    public static function is_pro_active() {
        return true; // Features work regardless of license
    }

    /**
     * Check if license is valid (for updates only).
     */
    public static function is_license_valid() {
        return 'valid' === get_option( 'edd_wbcom_your_plugin_license_status' );
    }

    /**
     * Check if specific feature is enabled.
     */
    public static function feature_enabled( $feature ) {
        return (bool) get_option( "your_plugin_feature_{$feature}", true );
    }
}
```

### Philosophy

- **Features work without license** - Better UX, users can use what they paid for
- **License required for updates only** - Via EDD updater class
- **Pro extends Free** - Pro is an addon, not a replacement

## Checklist for New Plugin

### Free Plugin

- [ ] Copy `admin/wbcom/` folder from existing plugin
- [ ] Update text domain in all files
- [ ] Create tab templates in `admin/tab-templates/`
- [ ] Enqueue wbcom styles and scripts
- [ ] Use correct HTML structure patterns
- [ ] Test toggle switches and form elements

### Pro Plugin (Addon)

- [ ] All Free Plugin steps above
- [ ] Copy `edd-license/` folder
- [ ] Update EDD constants (STORE_URL, ITEM_NAME, etc.)
- [ ] Rename updater class with plugin prefix
- [ ] Create `wbcom-paid-plugin-settings.php`
- [ ] Hook license section to `wbcom_add_plugin_license_code`
- [ ] Test license activation/deactivation
- [ ] Test plugin updates

## Common Issues

### Toggle Switch Not Saving

Ensure hidden input before checkbox:
```php
<input type="hidden" name="option_name" value="no" />
<input type="checkbox" name="option_name" value="yes" ... />
```

### License Page Not Showing

Check class exists guard:
```php
if ( ! class_exists( 'Wbcom_Paid_Plugin_Settings' ) ) {
    // Class definition
}
```

### CSS Variables Not Working

Ensure wbcom CSS is enqueued:
```php
wp_enqueue_style( 'wbcom-admin-setting', ... );
```

### Multiple Pro Plugins Conflict

Each Pro plugin should check class existence before defining `Wbcom_Paid_Plugin_Settings`.

---

## Related Skills

- `wp-plugin-development` - WordPress plugin patterns
- `wp-security-review` - Security best practices
- `code-review` - Code quality checks
