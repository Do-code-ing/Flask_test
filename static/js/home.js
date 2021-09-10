const jobSearchForm = document.getElementById("job_search_form");
const jobSearchText = document.getElementById("job_search_text");
const jobSearchBtn = document.getElementById("job_search_btn");
const searching = document.getElementById("searching");

searching.hidden = true;

function handleJobSearchBtnClick() {
  console.log(jobSearchText);
  if (jobSearchText.value) {
    jobSearchForm.hidden = true;
    searching.hidden = false;
  }
}

if (jobSearchBtn) {
  jobSearchBtn.addEventListener("click", handleJobSearchBtnClick);
}
