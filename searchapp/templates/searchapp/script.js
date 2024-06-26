const browseButton = document.getElementById("browseButton");
const fileInput = document.getElementById("fileInput");

browseButton.addEventListener("click", function(event) {
    fileInput.click();
    event.preventDefault();
});

fileInput.addEventListener("change", function() {
    const fileCardContainer = document.getElementById("fileCardContainer");
    const fileCardTemplate = document.getElementById("fileCardTemplate");

    // Clear existing file cards
    // fileCardContainer.innerHTML = "";

    for (const selectedFile of fileInput.files) {
        const fileCard = fileCardTemplate.cloneNode(true);
        fileCard.style.display = "block"; // Show the card
        fileCard.classList.add("file-card");

        // Update content with filename
        fileCard.querySelector("h2").textContent = selectedFile.name;

        // Optional: Update other content with file details (size, type, etc.)
        fileCard.querySelector("p").textContent = `Size: ${(selectedFile.size / 1024).toFixed(2)} KB`;

        fileCardContainer.appendChild(fileCard);
    }
});
