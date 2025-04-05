// export.js – For exporting resume section as PDF
document.getElementById('exportBtn').addEventListener('click', () => {
    const resume = document.getElementById('resume-content') || document.querySelector('.resume-template');

    const opt = {
        margin: 0.5,
        filename: 'my_resume.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    html2pdf().from(resume).set(opt).save();
});
