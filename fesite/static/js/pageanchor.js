  // Function to scroll to the "My Projects" section
  function scrollToProjectsSection() {
    const section = document.getElementById("formH");
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Listen for clicks on the "My Projects" link and scroll to the section
const myProjectsLink = document.querySelector('a[href="#formH"]');
if (myProjectsLink) {
    myProjectsLink.addEventListener('click', (event) => {
        event.preventDefault();
        scrollToProjectsSection();
    });
}