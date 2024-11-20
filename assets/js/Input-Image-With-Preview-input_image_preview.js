(function($) {
    //Image change
    $('.vInputImage').change(function(event) {
        let file = event.target.files[0];

        if (file) {
            // Set preview image
            let $parent = $(this).parent();
            let reader = new FileReader();

            reader.onload = function() {
                event.target.parentNode.style.backgroundImage = `url('${reader.result}')`;
            }

            reader.readAsDataURL(file);

            // Show reset button
            $parent.find('button').removeClass('d-none');

            // Fire custom event
            $parent.trigger('ip.img.change', [file, $parent.attr('input-data-index')]);
        }
    });

    //Clear
    $('.vClearPreviewImage').click(function(event) {
        let $parent = $(this).parent();
        event.currentTarget.classList.add('d-none');
        $parent.css('background-image', `url('/input_image_preview/upload_image.png')`);
        $parent.find('input').val(null);
        $parent.trigger('ip.img.clear', [$parent.attr('input-data-index')]);
    });
})(jQuery);