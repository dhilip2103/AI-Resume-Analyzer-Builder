// options.js – Handles real-time editing of resume
document.addEventListener('DOMContentLoaded', () => {
    const resumeArea = document.getElementById('resume-content') || document.querySelector('.resume-template');

    // Font Family
    document.getElementById('font-family').addEventListener('change', function () {
        resumeArea.style.fontFamily = this.value;
    });

    // Font Size
    document.getElementById('font-size').addEventListener('change', function () {
        resumeArea.style.fontSize = this.value + 'px';
    });

    // Font Color
    document.getElementById('font-color').addEventListener('change', function () {
        resumeArea.style.color = this.value;
    });

    // Highlight
    document.getElementById('highlight-color').addEventListener('change', function () {
        resumeArea.style.backgroundColor = this.value;
    });

    // Text formatting buttons
    document.querySelectorAll('.tool-btn[data-style]').forEach(button => {
        button.addEventListener('click', () => {
            const style = button.dataset.style;
            document.execCommand(style, false, null);
        });
    });

    // Clear Formatting
    document.getElementById('clear-formatting').addEventListener('click', () => {
        resumeArea.removeAttribute('style');
        resumeArea.innerHTML = resumeArea.innerText;
    });
});
