const recordList = document.getElementById('record-list');

    function saveRecord() {
        const medicalHistory = document.getElementById('medical-history').value;
        const allergies = document.getElementById('allergies').value;
        const diagnosis = document.getElementById('diagnosis').value;
        const date = new Date().toLocaleString();

        if (!medicalHistory && !allergies && !diagnosis) {
            alert('At least one field must be filled!');
            return;
        }

        const record = document.createElement('div');
        record.className = 'record';
        record.innerHTML = `
            <strong>Date:</strong> ${date}<br>
            <strong>Medical History:</strong> ${medicalHistory}<br>
            <strong>Allergies:</strong> ${allergies}<br>
            <strong>Diagnosis:</strong> ${diagnosis}
        `;

        recordList.appendChild(record);

        document.getElementById('health-form').reset();
    }