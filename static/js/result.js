"use strict";

const applyBtn = document.querySelectorAll(".result_apply_btn");
const upBtn = document.getElementById("page_up_btn");

function handleApplyBtnClick(event) {
  const url = event.target.attributes.url.value;
  window.open(url);
}

if (applyBtn) {
  applyBtn.forEach((btn) => {
    btn.addEventListener("click", handleApplyBtnClick);
  });
}
