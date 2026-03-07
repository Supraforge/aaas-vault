# Edit, Save, and Render Patterns

## Edit Component (Editor View)

```jsx
import { __ } from '@wordpress/i18n';
import {
    useBlockProps,
    RichText,
    InspectorControls,
    MediaUpload,
    MediaUploadCheck,
} from '@wordpress/block-editor';
import { PanelBody, TextControl, Button } from '@wordpress/components';
import './editor.scss';

export default function Edit( { attributes, setAttributes } ) {
    const { title, description, mediaId, mediaUrl } = attributes;

    const blockProps = useBlockProps( {
        className: 'feature-card',
    } );

    const onSelectMedia = ( media ) => {
        setAttributes( {
            mediaId: media.id,
            mediaUrl: media.url,
        } );
    };

    return (
        <>
            <InspectorControls>
                <PanelBody title={ __( 'Settings', 'myplugin' ) }>
                    <MediaUploadCheck>
                        <MediaUpload
                            onSelect={ onSelectMedia }
                            allowedTypes={ [ 'image' ] }
                            value={ mediaId }
                            render={ ( { open } ) => (
                                <Button onClick={ open } variant="secondary">
                                    { mediaUrl
                                        ? __( 'Replace Image', 'myplugin' )
                                        : __( 'Select Image', 'myplugin' )
                                    }
                                </Button>
                            ) }
                        />
                    </MediaUploadCheck>
                </PanelBody>
            </InspectorControls>

            <div { ...blockProps }>
                <RichText
                    tagName="h3"
                    className="feature-card__title"
                    value={ title }
                    onChange={ ( value ) => setAttributes( { title: value } ) }
                    placeholder={ __( 'Feature title...', 'myplugin' ) }
                />

                <RichText
                    tagName="p"
                    className="feature-card__description"
                    value={ description }
                    onChange={ ( value ) => setAttributes( { description: value } ) }
                    placeholder={ __( 'Feature description...', 'myplugin' ) }
                />
            </div>
        </>
    );
}
```

## Save Component (Static Blocks)

```jsx
import { useBlockProps, RichText } from '@wordpress/block-editor';

export default function Save( { attributes } ) {
    const { title, description, mediaUrl } = attributes;

    const blockProps = useBlockProps.save( {
        className: 'feature-card',
    } );

    return (
        <div { ...blockProps }>
            { mediaUrl && (
                <img
                    className="feature-card__image"
                    src={ mediaUrl }
                    alt=""
                />
            ) }

            { title && (
                <RichText.Content
                    tagName="h3"
                    className="feature-card__title"
                    value={ title }
                />
            ) }

            { description && (
                <RichText.Content
                    tagName="p"
                    className="feature-card__description"
                    value={ description }
                />
            ) }
        </div>
    );
}
```

## Dynamic Render (render.php)

```php
<?php
/**
 * Render callback for feature-card block.
 *
 * @param array    $attributes Block attributes.
 * @param string   $content    Block content.
 * @param WP_Block $block      Block instance.
 * @return string Rendered block HTML.
 */

$title       = $attributes['title'] ?? '';
$description = $attributes['description'] ?? '';
$media_url   = $attributes['mediaUrl'] ?? '';

$wrapper_attributes = get_block_wrapper_attributes( array(
    'class' => 'feature-card',
) );
?>

<div <?php echo $wrapper_attributes; ?>>
    <?php if ( $media_url ) : ?>
        <img class="feature-card__image" src="<?php echo esc_url( $media_url ); ?>" alt="">
    <?php endif; ?>

    <?php if ( $title ) : ?>
        <h3 class="feature-card__title"><?php echo esc_html( $title ); ?></h3>
    <?php endif; ?>

    <?php if ( $description ) : ?>
        <p class="feature-card__description"><?php echo wp_kses_post( $description ); ?></p>
    <?php endif; ?>
</div>
```

## Key Patterns

### useBlockProps()

Always use for wrapper element:

```jsx
// Editor
const blockProps = useBlockProps();
return <div { ...blockProps }>...</div>;

// Save
const blockProps = useBlockProps.save();
return <div { ...blockProps }>...</div>;

// PHP
$attrs = get_block_wrapper_attributes();
echo "<div {$attrs}>...</div>";
```

### When to Use Dynamic vs Static

**Static (save function):**
- Content doesn't change after save
- No server-side data needed
- Faster frontend (no PHP)

**Dynamic (render.php):**
- Needs current data (user info, post data)
- Content changes based on context
- Easier maintenance (no deprecations needed for markup changes)
