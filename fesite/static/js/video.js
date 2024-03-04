window.addEventListener('scroll', function() {
    var scrollTop = window.scrollY;
    var heroHeight = document.getElementById('webdev-video').offsetHeight; // Adjust to target your video element
    var video = document.getElementById('webdev-video'); // Change 'webdev-video' to your actual video ID
  
    if (scrollTop > heroHeight) {
      video.classList.add('video-small');
    } else {
      video.classList.remove('video-small');
    }
  });