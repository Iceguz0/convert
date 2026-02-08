document.getElementById("button").addEventListener("click", () => {
    const inputText = document.getElementById("text").value.trim();
    const outputDiv = document.getElementById("output");

    if (inputText) {
        // Convert each character to a 8-bit binary string
        const binaryValues = inputText.split('').map(char => {
            return char.charCodeAt(0).toString(2).padStart(8, '0');
        });

        outputDiv.innerText = binaryValues.join(" ");
        outputDiv.style.display = "block";
    } else {
        outputDiv.innerText = "";
        outputDiv.style.display = "none";
    }
});
