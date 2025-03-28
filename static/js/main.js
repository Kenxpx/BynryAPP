document.addEventListener('DOMContentLoaded', function() {
    // Real-time updates
    const eventSource = new EventSource('/updates/');
    
    eventSource.onmessage = function(e) {
        const data = JSON.parse(e.data);
        if (data.type === 'request_update') {
            updateRequestStatus(data.request_id, data.status);
        }
    };

    // Request status update handler
    function updateRequestStatus(requestId, newStatus) {
        const badge = document.querySelector(`#request-${requestId}-status`);
        if (badge) {
            badge.textContent = newStatus;
            badge.className = `status-badge status-${newStatus.toLowerCase()}`;
        }
    }

    // Guided Tour
    if (document.body.dataset.demoTour === 'true') {
        introJs().setOptions({
            steps: [{
                element: '#new-request-btn',
                intro: 'Click here to submit a new service request'
            }, {
                element: '#status-filter',
                intro: 'Filter requests by their current status'
            }]
        }).start();
    }

    // Attachment upload handler
    document.querySelectorAll('.file-upload').forEach(input => {
        input.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name || 'No file selected';
            this.nextElementSibling.textContent = fileName;
        });
    });
});