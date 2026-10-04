document.addEventListener("DOMContentLoaded", () => {
    const submitBtn = document.getElementById("submit");
    if (submitBtn) {
        submitBtn.addEventListener("click", predict);
    }
});

async function predict() {
    const textInput = document.getElementById("textarea").value;
    const resultElement = document.getElementById("result");
    const submitBtn = document.getElementById("submit");

    if (!textInput.trim()) {
        resultElement.innerText = "Please enter a review first!";
        return;
    }

    try {
        // UI feedback while loading
        submitBtn.disabled = true;
        resultElement.innerText = "Analyzing sentiment...";

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: textInput
            })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        resultElement.innerText = "Sentiment: " + data.prediction;
    } catch (error) {
        console.error("Error:", error);
        resultElement.innerText = "Error getting prediction. Check server logs.";
    } finally {
        submitBtn.disabled = false;
    }
}
