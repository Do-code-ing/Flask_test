"use strict";

const applyBtn = document.querySelectorAll(".result_apply_btn");
const upBtn = document.getElementById("page_up_btn");
const resultTbody = document.getElementById("result_tbody");

function handleApplyBtnClick(event) {
  const url = event.target.attributes.url.value;
  window.open(url);
}

function handleUpBtnClick() {
  resultTbody.scrollTo(0, 0);
}

if (applyBtn) {
  applyBtn.forEach((btn) => {
    btn.addEventListener("click", handleApplyBtnClick);
  });
}

if (upBtn) {
  upBtn.addEventListener("click", handleUpBtnClick);
}
