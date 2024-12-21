document.addEventListener('DOMContentLoaded', function() {
    const initialForm = document.getElementById('initial-form');
    
    if (initialForm) {
        initialForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const aadhar = document.getElementById('aadhar').value;
            const userType = document.querySelector('input[name="user-type"]:checked').value;
            
            // Validate Aadhar number (12 digits)
            if (!/^\d{12}$/.test(aadhar.replace(/\s/g, ''))) {
                showAlert('Please enter a valid 12-digit Aadhar number', 'error');
                return;
            }
            
            if (userType === 'healthcare') {
                window.location.href = 'healthcare-provider.html';
            } else {
                window.location.href = 'user-otp.html';
            }
        });
    }
    
    // OTP Verification
    const otpForm = document.getElementById('otp-form');
    if (otpForm) {
        otpForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const otp = document.getElementById('otp').value;
            
            // Validate OTP (6 digits)
            if (!/^\d{6}$/.test(otp)) {
                showAlert('Please enter a valid 6-digit OTP', 'error');
                return;
            }
            
            // Simulate OTP verification
            verifyOTP(otp);
        });
    }
    
    // Healthcare Provider Login
    const providerForm = document.getElementById('provider-form');
    if (providerForm) {
        providerForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const providerId = document.getElementById('provider-id').value;
            const password = document.getElementById('password').value;
            
            // Simulate provider authentication
            authenticateProvider(providerId, password);
        });
    }
});

function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = alert alert-${type};
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => alertDiv.remove(), 3000);
}

function verifyOTP(otp) {
    // Simulate OTP verification
    setTimeout(() => {
        if (otp === '123456') { // Demo purposes only
            window.location.href = 'user-dashboard.html';
        } else {
            showAlert('Invalid OTP. Please try again.', 'error');
        }
    }, 1000);
}

function authenticateProvider(providerId, password) {
    // Simulate authentication
    setTimeout(() => {
        if (providerId === 'DEMO123' && password === 'password') { // Demo purposes only
            window.location.href = 'healthcare-dashboard.html';
        } else {
            showAlert('Invalid credentials. Please try again.', 'error');
        }
    }, 1000);
}