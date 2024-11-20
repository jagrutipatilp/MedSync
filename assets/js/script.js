document.getElementById('chronicYes').addEventListener('click', () => {
      document.getElementById('chronicDetails').classList.remove('visually-hidden');
    });

    document.getElementById('chronicNo').addEventListener('click', () => {
      document.getElementById('chronicDetails').classList.add('visually-hidden');
    });

document.getElementById('fammedyes').addEventListener('click', () => {
      document.getElementById('familymedhistory').classList.remove('visually-hidden');
    });

    document.getElementById('fammedno').addEventListener('click', () => {
      document.getElementById('familymedhistory').classList.add('visually-hidden');
    });



document.getElementById('imageUploader').addEventListener('change', function(event) {
    const file = event.target.files[0]; // Get the selected file

    if (file) {
        const reader = new FileReader();

        // On file load, display the preview
        reader.onload = function(e) {
            const previewImage = document.getElementById('previewImage');
            previewImage.src = e.target.result; // Set image source to file data
            previewImage.classList.remove('d-none'); // Show the image
        };

        reader.readAsDataURL(file); // Read the file as a data URL
    }
});
