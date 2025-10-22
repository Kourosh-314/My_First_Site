
class NotificationManager {
    constructor() {
        this.autoRemoveTimeout = 5000; 
        this.animationDuration = 300; 
        this.init();
    }
    
    init() {
        this.autoRemoveAlerts();
        this.setupCloseButtons();
        this.setupAutoClose();
    }
    
    autoRemoveAlerts() {
        
        setTimeout(() => {
            const alerts = document.querySelectorAll('.alert');
            alerts.forEach(alert => {
                this.slideOutAndRemove(alert);
            });
        }, this.autoRemoveTimeout);
    }
    
    setupCloseButtons() {
        
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('close-btn')) {
                this.slideOutAndRemove(e.target.closest('.alert'));
            }
        });
    }
    
    setupAutoClose() {
        
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('alert') && !e.target.classList.contains('alert-dismissible')) {
                this.slideOutAndRemove(e.target);
            }
        });
    }
    
    slideOutAndRemove(element) {
        if (element && element.parentElement) {
            element.style.transition = `all ${this.animationDuration}ms ease`;
            element.style.transform = 'translateX(100%)';
            element.style.opacity = '0';
            
            setTimeout(() => {
                if (element.parentElement) {
                    element.remove();
                }
            }, this.animationDuration);
        }
    }
    
    
    showMessage(message, type = 'info', autoClose = true) {
        const notificationPopup = document.querySelector('.notification-popup');
        if (!notificationPopup) {
            console.error('Notification popup container not found');
            return;
        }
        
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible`;
        alertDiv.innerHTML = `
            <button type="button" class="close-btn">&times;</button>
            <div class="alert-content">${message}</div>
        `;
        
        notificationPopup.appendChild(alertDiv);
        
        
        if (autoClose) {
            setTimeout(() => {
                this.slideOutAndRemove(alertDiv);
            }, this.autoRemoveTimeout);
        }
        
        return alertDiv;
    }
    
    
    showFormErrors(errors) {
        if (!errors || errors.length === 0) return;
        
        let errorHtml = '<h4>Please fix the following errors:</h4><ul>';
        errors.forEach(error => {
            errorHtml += `<li>${error}</li>`;
        });
        errorHtml += '</ul>';
        
        this.showMessage(errorHtml, 'error');
    }
}


document.addEventListener('DOMContentLoaded', function() {
    window.notificationManager = new NotificationManager();
});


if (typeof module !== 'undefined' && module.exports) {
    module.exports = NotificationManager;
}