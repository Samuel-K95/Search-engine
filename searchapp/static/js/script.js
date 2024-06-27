document.getElementById('browseButton').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function() {
    const fileCardContainer = document.getElementById("fileCardContainer");
    const fileCardTemplate = document.getElementById("fileCardTemplate");


    for (const selectedFile of fileInput.files) {
        const fileCard = fileCardTemplate.content.cloneNode(true);
        fileCard.querySelector("h2").textContent = selectedFile.name;
        fileCard.querySelector("p").textContent = `Size: ${(selectedFile.size / 1024).toFixed(2)} KB`;

        fileCardContainer.appendChild(fileCard);
    }

    // Submit the form
    $('#uploadForm').submit();
});

$('#uploadForm').on('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);

    $.ajax({
        url: '/upload/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            console.log('Files uploaded successfully');
        },
        error: function(response) {
            console.error('An error occurred while uploading files.');
        }
    });
});
const paragraphs = [];

// Function to update paragraphs array with new content
function updateParagraph(rankedContent) {
    paragraphs.push(...rankedContent);
}

// Event listener for search form submission
document.querySelector('.search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch('/search/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.file_content) {
            updateParagraph(data.file_content);

            // Display the updated paragraphs
            const mainBody = document.body;
            mainBody.innerHTML = ""; // Clear the body content

            paragraphs.forEach((paragraph, index) => {
                const paragraphElement = document.createElement("p");
                paragraphElement.textContent = paragraph;
                paragraphElement.classList.add("paragraph-style"); // Add custom class for styling
                if (index < paragraphs.length - 1) {
                    paragraphElement.classList.add("paragraph-separator"); // Add separator class except for the last paragraph
                }
                mainBody.appendChild(paragraphElement);
            });
        } else {
            console.error('Invalid response format:', data);
        }
    })
    .catch(error => {
        console.error('An error occurred:', error);
    });
});
document.getElementById("searchButton").addEventListener("click", function () {
    const searchContainer = document.getElementById("searchContainer");
    const mainBody = document.body;

    // Ensure searchContainer is visible and at the top
    searchContainer.style.display = "block"; // Ensure it's visible
    searchContainer.classList.add("top-position"); // Apply top-position CSS

    // Move searchContainer to the top of mainBody
    mainBody.insertBefore(searchContainer, mainBody.firstChild);

    // Clear existing paragraphs if any
    const existingParagraphs = mainBody.querySelectorAll('.paragraph-style');
    existingParagraphs.forEach(paragraph => {
        paragraph.remove();
    });

    // Append new paragraphs based on 'paragraphs' array
    paragraphs.forEach((paragraph, index) => {
        const paragraphElement = document.createElement("p");
        paragraphElement.textContent = paragraph;
        paragraphElement.classList.add("paragraph-style");
        if (index < paragraphs.length - 1) {
            paragraphElement.classList.add("paragraph-separator");
        }
        mainBody.appendChild(paragraphElement);
    });
});



