"use strict";

const homeBtn = document.getElementById("home_btn");
const referenceBtn = document.getElementById("reference_btn");
const moreBtn = document.getElementById("more_btn");

function handleHomeBtnClick() {
  location.href = "/";
}

function handleReferenceBtnClick() {
  location.href = "/reference";
}

function handleMoreBtnClick() {
  location.href = "more";
}

if (homeBtn) {
  homeBtn.addEventListener("click", handleHomeBtnClick);
}

if (referenceBtn) {
  referenceBtn.addEventListener("click", handleReferenceBtnClick);
}

if (moreBtn) {
  moreBtn.addEventListener("click", handleMoreBtnClick);
}
