document.addEventListener('DOMContentLoaded', function() {
    function scrollCarousel(direction) {
        console.log("Button clicked:", direction);

        const carousel = document.getElementById("carousel");
        if (!carousel) {
            console.log("Carousel not found");
            return;
        }

        carousel.scrollBy({
            left: 220 * direction,
            behavior: "smooth"
        });
    }

    // Export the function to the global scope
    window.scrollCarousel = scrollCarousel;
});
