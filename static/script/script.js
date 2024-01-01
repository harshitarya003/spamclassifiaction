// script.js

function copyToClipboard(event) {
    // Get the parent card element of the clicked copy icon
    var card = event.target.closest('.card');

    if (!card) {
        console.error('Card not found');
        return;
    }

    // Get the text content of the card-content div within the clicked card
    var cardContent = card.querySelector('.card-content');
    var textToCopy = cardContent.textContent || cardContent.innerText;

    // Create a textarea element to temporarily hold the text
    var textArea = document.createElement('textarea');
    textArea.value = textToCopy;
    document.body.appendChild(textArea);

    // Select and copy the text
    textArea.select();
    document.execCommand('copy');

    // Remove the textarea from the DOM
    document.body.removeChild(textArea);

    // Provide feedback to the user that the text has been copied if needed
    alert('Content copied to clipboard!');
}
