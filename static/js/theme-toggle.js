(function () {
  var root = document.documentElement;
  var toggles = document.querySelectorAll("[data-theme-toggle]");
  var storageKey = "theme";
  var nightStartsAt = 18;
  var dayStartsAt = 7;

  function getStoredTheme() {
    var stored = null;
    try {
      stored = localStorage.getItem(storageKey);
    } catch (e) {
      stored = null;
    }
    if (stored === "dark" || stored === "light") {
      return stored;
    }
    return null;
  }

  function setStoredTheme(theme) {
    try {
      localStorage.setItem(storageKey, theme);
    } catch (e) {
      // ignore write errors (e.g., private mode)
    }
  }

  function getPreferredTheme() {
    if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    }
    return "light";
  }

  function getTimeBasedTheme() {
    var hour = new Date().getHours();
    if (hour >= nightStartsAt || hour < dayStartsAt) {
      return "dark";
    }
    return "light";
  }

  function resolveInitialTheme() {
    var storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }

    var currentAttr = root.getAttribute("data-theme");
    if (currentAttr === "dark" || currentAttr === "light") {
      return currentAttr;
    }

    return getTimeBasedTheme() || getPreferredTheme();
  }

  function updateToggles(theme) {
    var isDark = theme === "dark";
    var label = isDark ? "Switch to light mode" : "Switch to dark mode";
    var i;
    for (i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute("aria-pressed", isDark ? "true" : "false");
      toggles[i].setAttribute("aria-label", label);
    }
  }

  function applyTheme(theme, persist) {
    root.setAttribute("data-theme", theme);
    updateToggles(theme);
    if (persist) {
      setStoredTheme(theme);
    }
  }

  var currentTheme = resolveInitialTheme();
  applyTheme(currentTheme, false);

  function handleToggle() {
    var nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(nextTheme, true);
  }

  var i;
  for (i = 0; i < toggles.length; i++) {
    toggles[i].addEventListener("click", handleToggle);
  }

  if (window.matchMedia) {
    var media = window.matchMedia("(prefers-color-scheme: dark)");
    var onChange = function (event) {
      if (getStoredTheme()) {
        return;
      }
      var timeTheme = getTimeBasedTheme();
      var nextTheme = timeTheme || (event.matches ? "dark" : "light");
      applyTheme(nextTheme, false);
    };
    if (media.addEventListener) {
      media.addEventListener("change", onChange);
    } else if (media.addListener) {
      media.addListener(onChange);
    }
  }
})();
