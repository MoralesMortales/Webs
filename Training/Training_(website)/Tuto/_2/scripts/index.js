const starEl = document.querySelectorAll(".fa-star");
const emojisEl = document.querySelectorAll(".fa-regular");
 
// console.log(starEl);

starEl.forEach((starEl, position) =>  {
    starEl.addEventListener("click", () => {
        updateRating(position);
    })

})

function updateRating(position){
    starEl.forEach((starEl,idx) => {
            if (idx < (position + 1)) {
                starEl.classList.add("active");
            }

            else{
                starEl.classList.remove("active");
            }
    }
);

emojisEl.forEach((emojisEl) => {

    emojisEl.style.transform = `translateX(-${position * 48}px)`;
}

)};
