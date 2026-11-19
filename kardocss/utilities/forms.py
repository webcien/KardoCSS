"""
Generador de utilidades para formularios modernos en KardoCSS
"""

def generate_form_utilities():
    """Genera utilidades CSS para formularios modernos"""
    css = []
    
    # Input y textarea base
    css.append("""
/* ==========================================================================
   FORM UTILITIES
   ========================================================================== */

/* Input base moderno */
.k-input {
    display: block;
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    line-height: 1.5;
    color: var(--k-text);
    background-color: var(--k-surface);
    border: 1px solid var(--k-border);
    border-radius: 0.5rem;
    transition: all 0.2s ease;
}

.k-input:focus {
    outline: none;
    border-color: var(--k-primary);
    box-shadow: 0 0 0 3px var(--k-focus-ring);
}

.k-input:disabled {
    background-color: var(--k-surface-3);
    cursor: not-allowed;
    opacity: 0.6;
}

.k-input::placeholder {
    color: var(--k-placeholder);
}

/* Textarea moderno */
.k-textarea {
    display: block;
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    line-height: 1.5;
    color: var(--k-text);
    background-color: var(--k-surface);
    border: 1px solid var(--k-border);
    border-radius: 0.5rem;
    transition: all 0.2s ease;
    resize: vertical;
    min-height: 100px;
}

.k-textarea:focus {
    outline: none;
    border-color: var(--k-primary);
    box-shadow: 0 0 0 3px var(--k-focus-ring);
}

/* Select moderno */
.k-select {
    display: block;
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    line-height: 1.5;
    color: var(--k-text);
    background-color: var(--k-surface);
    border: 1px solid var(--k-border);
    border-radius: 0.5rem;
    transition: all 0.2s ease;
    cursor: pointer;
}

.k-select:focus {
    outline: none;
    border-color: var(--k-primary);
    box-shadow: 0 0 0 3px var(--k-focus-ring);
}

/* Label moderno */
.k-label {
    display: block;
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--k-text);
    margin-bottom: 0.5rem;
}

/* Form group */
.k-form-group {
    margin-bottom: 1.5rem;
}

/* Input con icono */
.k-input-group {
    position: relative;
    display: flex;
    align-items: center;
}

.k-input-icon {
    position: absolute;
    left: 1rem;
    color: var(--k-placeholder);
    pointer-events: none;
}

.k-input-with-icon {
    padding-left: 2.75rem;
}

/* Tamaños de input */
.k-input-sm {
    padding: 0.5rem 0.75rem;
    font-size: 0.875rem;
}

.k-input-lg {
    padding: 1rem 1.25rem;
    font-size: 1.125rem;
}

/* Input con error */
.k-input-error {
    border-color: var(--k-danger);
}

.k-input-error:focus {
    border-color: var(--k-danger);
    box-shadow: 0 0 0 3px var(--k-danger-soft);
}

/* Input con éxito */
.k-input-success {
    border-color: var(--k-success);
}

.k-input-success:focus {
    border-color: var(--k-success);
    box-shadow: 0 0 0 3px var(--k-success-soft);
}

/* Mensaje de error */
.k-error-message {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.875rem;
    color: var(--k-danger);
}

/* Mensaje de ayuda */
.k-help-text {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.875rem;
    color: var(--k-text-muted);
}

/* Checkbox y radio modernos */
.k-checkbox,
.k-radio {
    width: 1.25rem;
    height: 1.25rem;
    border: 2px solid var(--k-border);
    border-radius: 0.25rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.k-radio {
    border-radius: 50%;
}

.k-checkbox:checked,
.k-radio:checked {
    background-color: var(--k-primary);
    border-color: var(--k-primary);
}

.k-checkbox:focus,
.k-radio:focus {
    outline: none;
    box-shadow: 0 0 0 3px var(--k-focus-ring);
}

/* Switch toggle */
.k-switch {
    position: relative;
    display: inline-block;
    width: 3rem;
    height: 1.75rem;
}

.k-switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.k-switch-slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: var(--k-border);
    transition: 0.3s;
    border-radius: 1.75rem;
}

.k-switch-slider:before {
    position: absolute;
    content: "";
    height: 1.25rem;
    width: 1.25rem;
    left: 0.25rem;
    bottom: 0.25rem;
    background-color: var(--k-text-inverse);
    transition: 0.3s;
    border-radius: 50%;
}

.k-switch input:checked + .k-switch-slider {
    background-color: var(--k-primary);
}

.k-switch input:checked + .k-switch-slider:before {
    transform: translateX(1.25rem);
}

/* Botones modernos */
.k-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.5;
    text-align: center;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-decoration: none;
}

.k-btn:hover {
    transform: translateY(-1px);
    box-shadow: var(--k-shadow-md);
}

.k-btn:active {
    transform: translateY(0);
}

.k-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.k-btn-primary {
    background-color: var(--k-primary);
    color: var(--k-text-inverse);
}

.k-btn-primary:hover {
    background-color: var(--k-primary-hover);
}

.k-btn-secondary {
    background-color: var(--k-text-muted);
    color: var(--k-text-inverse);
}

.k-btn-secondary:hover {
    background-color: var(--k-text);
}

.k-btn-success {
    background-color: var(--k-success);
    color: var(--k-text-inverse);
}

.k-btn-success:hover {
    background-color: var(--k-success-hover);
}

.k-btn-danger {
    background-color: var(--k-danger);
    color: var(--k-text-inverse);
}

.k-btn-danger:hover {
    background-color: var(--k-danger-hover);
}

.k-btn-outline {
    background-color: transparent;
    border: 2px solid var(--k-primary);
    color: var(--k-primary);
}

.k-btn-outline:hover {
    background-color: var(--k-primary);
    color: var(--k-text-inverse);
}

/* Tamaños de botones */
.k-btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}

.k-btn-lg {
    padding: 1rem 2rem;
    font-size: 1.125rem;
}

.k-btn-block {
    display: flex;
    width: 100%;
}

/* Form layout */
.k-form-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.k-form-col {
    flex: 1;
}

@media (max-width: 768px) {
    .k-form-row {
        flex-direction: column;
    }
}

/* Fieldset moderno */
.k-fieldset {
    border: 1px solid var(--k-divider);
    border-radius: 0.5rem;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.k-legend {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--k-text);
    padding: 0 0.5rem;
}

/* File input moderno */
.k-file-input {
    display: block;
    width: 100%;
    padding: 0.75rem;
    border: 2px dashed var(--k-border);
    border-radius: 0.5rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.k-file-input:hover {
    border-color: var(--k-primary);
    background-color: var(--k-info-soft);
}

/* Input con contador de caracteres */
.k-input-counter {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 0.5rem;
    font-size: 0.875rem;
    color: var(--k-text-muted);
}

/* Validación en tiempo real */
.k-input.k-validating {
    border-color: var(--k-warning);
}

.k-input.k-valid {
    border-color: var(--k-success);
}

.k-input.k-invalid {
    border-color: var(--k-danger);
}

/* Loading state */
.k-input-loading {
    position: relative;
}

.k-input-loading::after {
    content: "";
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    width: 1rem;
    height: 1rem;
    border: 2px solid var(--k-divider);
    border-top-color: var(--k-primary);
    border-radius: 50%;
    animation: k-spin 0.6s linear infinite;
}

@keyframes k-spin {
    to { transform: translateY(-50%) rotate(360deg); }
}
""")
    
    return "\n".join(css)


if __name__ == "__main__":
    print(generate_form_utilities())

