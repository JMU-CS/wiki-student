document.addEventListener("DOMContentLoaded", function () {
  // DokuWiki replaced spaces with underscores
  const oldHash = window.location.hash;
  if (oldHash.includes('_')) {

    // Zensical uses dashes and all-lowercase
    const newHash = oldHash.replace(/_/g, '-').toLowerCase();

    // Update the URL without reloading the page
    history.replaceState(null, '', newHash);

    // Manually scroll to the element (if needed)
    const element = document.querySelector(newHash);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
});
