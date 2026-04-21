// Student CRUD App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Confirm delete action
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const studentName = this.getAttribute('data-name');
            if (!confirm(`Are you sure you want to delete ${studentName}?`)) {
                e.preventDefault();
            }
        });
    });

    // Auto-hide alerts after 3 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 3000);
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const nameInput = form.querySelector('input[name="name"]');
            const emailInput = form.querySelector('input[name="email"]');

            if (nameInput && !nameInput.value.trim()) {
                alert('Name is required');
                e.preventDefault();
                return;
            }

            if (emailInput && !emailInput.value.trim()) {
                alert('Email is required');
                e.preventDefault();
                return;
            }

            // Basic email validation
            if (emailInput && !isValidEmail(emailInput.value)) {
                alert('Please enter a valid email address');
                e.preventDefault();
                return;
            }
        });
    });
});

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}