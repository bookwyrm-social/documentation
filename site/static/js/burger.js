document.addEventListener('DOMContentLoaded', () => {
    // Get "navbar-burger" element
    const el = document.querySelector('.navbar-burger');

    // Add a click event
    el.addEventListener('click', () => {

        // Get the targets from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
    });
});
