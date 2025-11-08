// Mobile Menu Toggle
document.querySelector('.mobile-toggle').addEventListener('click',()=> {
    document.querySelector('.nav-menu').classList.toggle('active');
});

// Close menu on click
document.querySelectorAll('.nav-menu a').forEach(a=>{
    a.addEventListener('click',()=>document.querySelector('.nav-menu').classList.remove('active'));
});

// Carousel Functionality (if exists on page)
const carouselSlides = document.querySelector('.carousel-slides');
if (carouselSlides) {
    const carouselDots = document.querySelectorAll('.carousel-dot');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');
    let currentSlide = 0;
    const totalSlides = 4;

    // Function to update carousel
    function updateCarousel() {
        carouselSlides.style.transform = `translateX(-${currentSlide * 25}%)`;
        
        // Update active dot
        carouselDots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentSlide);
        });
    }

    // Next slide
    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateCarousel();
    }

    // Previous slide
    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateCarousel();
    }

    // Event listeners
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    // Dot navigation
    carouselDots.forEach(dot => {
        dot.addEventListener('click', () => {
            currentSlide = parseInt(dot.getAttribute('data-index'));
            updateCarousel();
        });
    });

    // Auto slide every 5 seconds
    setInterval(nextSlide, 5000);
}