
let currentSlide = 0;
const slider = document.getElementById('slider');
const totalSlides = document.querySelectorAll('section').length;
const progress = document.getElementById('progress');

function updateSlide() {
    slider.style.transform = `translateX(-${currentSlide * 100}vw)`;
    progress.style.width = `${((currentSlide + 1) / totalSlides) * 100}%`;
    
    // Add active class for animations
    document.querySelectorAll('section').forEach((s, i) => {
        if(i === currentSlide) s.classList.add('active');
        else s.classList.remove('active');
    });
}

function moveSlide(direction) {
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    updateSlide();
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') moveSlide(1);
    if (e.key === 'ArrowLeft') moveSlide(-1);
});

// Initialize
updateSlide();
