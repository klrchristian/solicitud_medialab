document.addEventListener('DOMContentLoaded', function() {
    // Validación de Bootstrap
    (function() {
        'use strict';
        const forms = document.querySelectorAll('.needs-validation');
        if (forms.length > 0) {
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }
    })();

    // Mostrar Toast y luego enviar el formulario
    const mainForm = document.querySelector('.needs-validation');
    if (mainForm) {
        mainForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const toastElement = document.getElementById('liveToast');
            
            if (toastElement) {
                const toast = new bootstrap.Toast(toastElement);
                toast.show();

                setTimeout(() => {
                    this.submit();
                }, 3000);
            } else {
                this.submit();
            }
        });
    }

    // Inicializar tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipTriggerList.length > 0) {
        tooltipTriggerList.forEach(function(tooltipTriggerEl) {
            new bootstrap.Tooltip(tooltipTriggerEl, {
                customClass: 'custom-tooltip',
                container: 'body',
                trigger: 'hover focus'
            });
        });
    }

    // Manejar el cierre de tooltips en touchstart
    document.addEventListener('touchstart', function(e) {
        tooltipTriggerList.forEach(function(tooltipTriggerEl) {
            var tooltipInstance = bootstrap.Tooltip.getInstance(tooltipTriggerEl);
            if (tooltipInstance) {
                tooltipInstance.hide();
            }
        });
    });

    // Establecer la fecha actual
    const fechaInput = document.getElementById('fSolicitud');
    if (fechaInput) {
        const hoy = new Date().toISOString().split('T')[0];
        fechaInput.value = hoy;
    }
});

// Funciones auxiliares fuera del DOMContentLoaded
function updateAdditionalOptions() {
    const checkboxes = document.querySelectorAll('input[name="options[]"]:checked');
    const container = document.getElementById('additional-options-container');
    
    if (container) {
        container.innerHTML = '';
        checkboxes.forEach(checkbox => {
            const additionalDiv = document.createElement('div');
            additionalDiv.className = 'additional-option';
            additionalDiv.id = `additional-${checkbox.value}`;
            additionalDiv.innerHTML = generateAdditionalOptions(checkbox.value);
            container.appendChild(additionalDiv);
        });
    }
}

function toggleSection(header) {
    if (header && header.parentElement) {
        header.parentElement.classList.toggle('active');
    }
}

// Mantener generateAdditionalOptions como está
function generateAdditionalOptions(option) {
    const optionsConfig = {
        'option1': {
            title: 'Opciones adicionales para Transmisión en vivo (Público):',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra1-1`, value: 'extra1-1', label: 'Autorizo la publicación del material', checked: true, disabled: false },
                { id: `${option}_extra1-2`, value: 'extra1-2', label: 'Extra 1-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option2': {
            title: 'Opciones adicionales para Opción 2:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra2-1`, value: 'extra2-1', label: 'Extra 2-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra2-2`, value: 'extra2-2', label: 'Extra 2-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option3': {
            title: 'Opciones adicionales para Opción 3:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra3-1`, value: 'extra3-1', label: 'Extra 3-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra3-2`, value: 'extra3-2', label: 'Extra 3-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option4': {
            title: 'Opciones adicionales para Opción 4:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra4-1`, value: 'extra4-1', label: 'Extra 4-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra4-2`, value: 'extra4-2', label: 'Extra 4-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option5': {
            title: 'Opciones adicionales para Opción 5:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra5-1`, value: 'extra5-1', label: 'Extra 5-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra5-2`, value: 'extra5-2', label: 'Extra 5-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option6': {
            title: 'Opciones adicionales para Opción 6:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra6-1`, value: 'extra6-1', label: 'Extra 6-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra6-2`, value: 'extra6-2', label: 'Extra 6-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option7': {
            title: 'Opciones adicionales para Opción 7:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra7-1`, value: 'extra7-1', label: 'Extra 7-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra7-2`, value: 'extra7-2', label: 'Extra 7-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option8': {
            title: 'Opciones adicionales para Opción 8:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra8-1`, value: 'extra8-1', label: 'Extra 8-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra8-2`, value: 'extra8-2', label: 'Extra 8-2', tooltip: 'Lorem ipsum...' }
            ]
        },
        'option9': {
            title: 'Opciones adicionales para Opción 9:',
            description: 'Este servicio ofrece soporte técnico durante el evento para garantizar que todo funcione correctamente.',
            options: [
                { id: `${option}_extra9-1`, value: 'extra9-1', label: 'Extra 9-1', tooltip: 'Lorem ipsum...' },
                { id: `${option}_extra9-2`, value: 'extra9-2', label: 'Extra 9-2', tooltip: 'Lorem ipsum...' }
            ]
        }
    };

    const config = optionsConfig[option];
    if (!config) return '';

    const optionsHTML = config.options.map(opt => `
        <div class="option-item">
            <div class="option-content">
                <input type="checkbox" 
                    id="${opt.id}" 
                    name="${option}_extras[]" 
                    value="${opt.value}" 
                    class="form-check-input"
                    ${opt.checked ? 'checked' : ''}
                    ${opt.disabled ? 'disabled' : ''}>
                <label for="${opt.id}" class="form-check-label">${opt.label}</label>
            </div>
            ${opt.tooltip ? `
                <span class="help-icon dynamic-tooltip" data-bs-toggle="tooltip" title="${opt.tooltip}">?</span>
            ` : ''}
        </div>
    `).join('');

    return `
        <h4 class="mt-4">${config.title}</h4>
        ${config.description ? `<p class="option-description">${config.description}</p>` : ''}
        <div class="options-grid">
            ${optionsHTML}
        </div>
    `;
}
