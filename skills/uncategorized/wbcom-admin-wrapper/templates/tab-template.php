<?php
/**
 * Tab content template.
 *
 * Copy this file to: admin/tab-templates/your-setting-{tab-slug}-tab.php
 *
 * @package Your_Plugin
 */

// Exit if accessed directly.
defined( 'ABSPATH' ) || exit;
?>
<div class="wbcom-tab-content">
	<div class="wbcom-wrapper-admin">
		<!-- Title Section -->
		<div class="wbcom-admin-title-section">
			<h3><?php esc_html_e( 'Tab Title', 'your-text-domain' ); ?></h3>
		</div>

		<!-- Options Container -->
		<div class="wbcom-admin-option-wrap wbcom-admin-option-wrap-view">
			<form method="post" action="options.php">
				<?php
				// Register your settings group in admin class.
				settings_fields( 'your_settings_group' );
				?>

				<!-- Toggle Switch Setting -->
				<div class="wbcom-settings-section-wrap">
					<div class="wbcom-settings-section-options-heading">
						<label for="enable_feature">
							<?php esc_html_e( 'Enable Feature', 'your-text-domain' ); ?>
						</label>
						<p class="description">
							<?php esc_html_e( 'Turn this feature on or off.', 'your-text-domain' ); ?>
						</p>
					</div>
					<div class="wbcom-settings-section-options">
						<div class="wb-admin-switch">
							<input type="hidden" name="your_enable_feature" value="no" />
							<input
								type="checkbox"
								id="enable_feature"
								name="your_enable_feature"
								value="yes"
								<?php checked( 'yes', get_option( 'your_enable_feature', 'yes' ) ); ?>
							/>
							<label for="enable_feature"></label>
						</div>
					</div>
				</div>

				<!-- Select Dropdown Setting -->
				<div class="wbcom-settings-section-wrap">
					<div class="wbcom-settings-section-options-heading">
						<label for="display_mode">
							<?php esc_html_e( 'Display Mode', 'your-text-domain' ); ?>
						</label>
						<p class="description">
							<?php esc_html_e( 'Choose how content should be displayed.', 'your-text-domain' ); ?>
						</p>
					</div>
					<div class="wbcom-settings-section-options">
						<select name="your_display_mode" id="display_mode">
							<option value="grid" <?php selected( 'grid', get_option( 'your_display_mode', 'grid' ) ); ?>>
								<?php esc_html_e( 'Grid', 'your-text-domain' ); ?>
							</option>
							<option value="list" <?php selected( 'list', get_option( 'your_display_mode' ) ); ?>>
								<?php esc_html_e( 'List', 'your-text-domain' ); ?>
							</option>
							<option value="compact" <?php selected( 'compact', get_option( 'your_display_mode' ) ); ?>>
								<?php esc_html_e( 'Compact', 'your-text-domain' ); ?>
							</option>
						</select>
					</div>
				</div>

				<!-- Number Input Setting -->
				<div class="wbcom-settings-section-wrap">
					<div class="wbcom-settings-section-options-heading">
						<label for="items_per_page">
							<?php esc_html_e( 'Items Per Page', 'your-text-domain' ); ?>
						</label>
						<p class="description">
							<?php esc_html_e( 'Number of items to show per page.', 'your-text-domain' ); ?>
						</p>
					</div>
					<div class="wbcom-settings-section-options">
						<input
							type="number"
							id="items_per_page"
							name="your_items_per_page"
							min="1"
							max="100"
							value="<?php echo esc_attr( get_option( 'your_items_per_page', 10 ) ); ?>"
						/>
					</div>
				</div>

				<!-- Submit Button -->
				<div class="wbcom-settings-section-wrap">
					<?php submit_button( __( 'Save Settings', 'your-text-domain' ) ); ?>
				</div>

			</form>
		</div>
	</div>
</div>
