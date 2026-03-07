<?php
/**
 * Wbcom Wrapper - Settings Row Templates
 *
 * Copy-paste templates for common settings patterns.
 *
 * @package Wbcom_Admin_Wrapper
 */

// ============================================================================
// TOGGLE SWITCH
// ============================================================================
?>
<!-- Toggle Switch Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label for="your_option_id">
			<?php esc_html_e( 'Enable Feature', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Description of what this toggle does.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<div class="wb-admin-switch">
			<input type="hidden" name="your_option_name" value="no" />
			<input
				type="checkbox"
				id="your_option_id"
				name="your_option_name"
				value="yes"
				<?php checked( 'yes', get_option( 'your_option_name', 'yes' ) ); ?>
			/>
			<label for="your_option_id"></label>
		</div>
	</div>
</div>

<?php
// ============================================================================
// SELECT DROPDOWN
// ============================================================================
?>
<!-- Select Dropdown Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label for="your_select_id">
			<?php esc_html_e( 'Choose Option', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Select your preferred option.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<select name="your_select_name" id="your_select_id">
			<option value="option1" <?php selected( 'option1', get_option( 'your_select_name', 'option1' ) ); ?>>
				<?php esc_html_e( 'Option 1', 'your-text-domain' ); ?>
			</option>
			<option value="option2" <?php selected( 'option2', get_option( 'your_select_name' ) ); ?>>
				<?php esc_html_e( 'Option 2', 'your-text-domain' ); ?>
			</option>
			<option value="option3" <?php selected( 'option3', get_option( 'your_select_name' ) ); ?>>
				<?php esc_html_e( 'Option 3', 'your-text-domain' ); ?>
			</option>
		</select>
	</div>
</div>

<?php
// ============================================================================
// RADIO BUTTONS
// ============================================================================
?>
<!-- Radio Buttons Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label>
			<?php esc_html_e( 'Select Mode', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Choose how this feature should work.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<label class="wbcom-radio-option">
			<input type="radio" name="your_radio_name" value="mode1"
				<?php checked( 'mode1', get_option( 'your_radio_name', 'mode1' ) ); ?> />
			<?php esc_html_e( 'Mode 1 - Description', 'your-text-domain' ); ?>
		</label>
		<label class="wbcom-radio-option">
			<input type="radio" name="your_radio_name" value="mode2"
				<?php checked( 'mode2', get_option( 'your_radio_name' ) ); ?> />
			<?php esc_html_e( 'Mode 2 - Description', 'your-text-domain' ); ?>
		</label>
		<label class="wbcom-radio-option">
			<input type="radio" name="your_radio_name" value="mode3"
				<?php checked( 'mode3', get_option( 'your_radio_name' ) ); ?> />
			<?php esc_html_e( 'Mode 3 - Description', 'your-text-domain' ); ?>
		</label>
	</div>
</div>

<?php
// ============================================================================
// TEXT INPUT
// ============================================================================
?>
<!-- Text Input Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label for="your_text_id">
			<?php esc_html_e( 'Text Setting', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Enter a value for this setting.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<input
			type="text"
			id="your_text_id"
			name="your_text_name"
			class="regular-text"
			value="<?php echo esc_attr( get_option( 'your_text_name', '' ) ); ?>"
		/>
	</div>
</div>

<?php
// ============================================================================
// NUMBER INPUT
// ============================================================================
?>
<!-- Number Input Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label for="your_number_id">
			<?php esc_html_e( 'Number Setting', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Enter a number value.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<input
			type="number"
			id="your_number_id"
			name="your_number_name"
			min="0"
			max="100"
			step="1"
			value="<?php echo esc_attr( get_option( 'your_number_name', 10 ) ); ?>"
		/>
	</div>
</div>

<?php
// ============================================================================
// TEXTAREA
// ============================================================================
?>
<!-- Textarea Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label for="your_textarea_id">
			<?php esc_html_e( 'Long Text', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Enter multiple lines of text.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<textarea
			id="your_textarea_id"
			name="your_textarea_name"
			rows="4"
			class="large-text"
		><?php echo esc_textarea( get_option( 'your_textarea_name', '' ) ); ?></textarea>
	</div>
</div>

<?php
// ============================================================================
// CHECKBOX GRID (2 COLUMNS)
// ============================================================================
?>
<!-- Checkbox Grid Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label>
			<?php esc_html_e( 'Select Options', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Choose which options to enable.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<?php
		$selected = get_option( 'your_multi_option', array() );
		$options  = array(
			'option1' => __( 'Option 1', 'your-text-domain' ),
			'option2' => __( 'Option 2', 'your-text-domain' ),
			'option3' => __( 'Option 3', 'your-text-domain' ),
			'option4' => __( 'Option 4', 'your-text-domain' ),
		);
		?>
		<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
			<?php foreach ( $options as $value => $label ) : ?>
				<label class="wbcom-checkbox-option">
					<input
						type="checkbox"
						name="your_multi_option[]"
						value="<?php echo esc_attr( $value ); ?>"
						<?php checked( in_array( $value, (array) $selected, true ) ); ?>
					/>
					<?php echo esc_html( $label ); ?>
				</label>
			<?php endforeach; ?>
		</div>
	</div>
</div>

<?php
// ============================================================================
// CHECKBOX GRID (3 COLUMNS)
// ============================================================================
?>
<!-- Checkbox Grid 3 Columns Setting -->
<div class="wbcom-settings-section-wrap">
	<div class="wbcom-settings-section-options-heading">
		<label>
			<?php esc_html_e( 'Skills / Tags', 'your-text-domain' ); ?>
		</label>
		<p class="description">
			<?php esc_html_e( 'Select items to enable.', 'your-text-domain' ); ?>
		</p>
	</div>
	<div class="wbcom-settings-section-options">
		<?php
		$selected = get_option( 'your_skills_option', array() );
		$items    = array(
			'item1' => __( 'Item 1', 'your-text-domain' ),
			'item2' => __( 'Item 2', 'your-text-domain' ),
			'item3' => __( 'Item 3', 'your-text-domain' ),
			'item4' => __( 'Item 4', 'your-text-domain' ),
			'item5' => __( 'Item 5', 'your-text-domain' ),
			'item6' => __( 'Item 6', 'your-text-domain' ),
		);
		?>
		<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
			<?php foreach ( $items as $value => $label ) : ?>
				<label class="wbcom-checkbox-option">
					<input
						type="checkbox"
						name="your_skills_option[]"
						value="<?php echo esc_attr( $value ); ?>"
						<?php checked( in_array( $value, (array) $selected, true ) ); ?>
					/>
					<?php echo esc_html( $label ); ?>
				</label>
			<?php endforeach; ?>
		</div>
	</div>
</div>

<?php
// ============================================================================
// SUBMIT BUTTON
// ============================================================================
?>
<!-- Submit Button -->
<div class="wbcom-settings-section-wrap">
	<?php submit_button( __( 'Save Settings', 'your-text-domain' ) ); ?>
</div>
