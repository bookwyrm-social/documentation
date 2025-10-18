document.addEventListener('DOMContentLoaded', () => {
    const languageSelector = document.getElementById("language_selection");
    languageSelector.onchange = function(event) {
        var current_location = window.location.pathname;
        var locale_index = current_location.indexOf(current_locale);
        var new_location = "/" + event.target.value;

        if (locale_index) {
            // we're in a locale - swap it out
            new_location = current_location.replace(current_locale, event.target.value)
        } else {
            // are we in a version?
            var regx = /\/v[0-9\.]+/
            if (regx.test(current_location)) {
                // split current location
                arr = current_location.split("/")
                // insert new locale
                arr.splice(2, 0, event.target.value.replace("/", ""))
                // gather it all together again
                new_location = arr.join("/")
            } else {
                new_location += current_location.slice(1);
            }
        }
        window.location = new_location;
    }

    // SELECT VERSION
    var versionSelector = document.getElementById("version_selection");
    versionSelector.onchange = function(event) {
        current_version = "{{ current_version|safe }}"
        var current_location = window.location.pathname;
        var target_version = event.target.value == "development" ? "" : event.target.value;
        var arr = current_location.split("/")
        var regx = /\/v[0-9\.]+/
        if (regx.test(current_location)) {
            window.location = window.location.href.replace(regx,`/${target_version}`)
        } else {
            window.location = `/${target_version}${current_location}`
        }
    }

    // SHOW/HIDE MENU
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {

            // Get the targets from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);
            const $menuTarget = document.getElementById('menu');

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
            // toggle hidden class on menu
            $menuTarget.classList.toggle('is-hidden-touch');
        });
    });

    // Table of contents
    const $tocController = document.getElementById("toc");
    if ($tocController) {
        $tocController.addEventListener('click', () => {
            $tocController.classList.toggle('is-active');
            const target = $tocController.dataset.target;
            const $target = document.getElementById(target);
            $target.classList.toggle('is-hidden-touch');
        })
    }

});
