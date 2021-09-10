"use strict";

const upBtn = document.getElementById("page_up_btn");

if (upBtn) {
  upBtn.addEventListener("click", () => {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  });
}
