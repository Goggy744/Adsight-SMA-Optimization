
const label = document.getElementById("label");
const submitBtn = document.getElementById("submit-btn");
const frenchFlag = document.getElementById("french-flag");
const englishFlag = document.getElementById("english-flag");

function languageManagement() {
  if (frenchFlag.classList.contains("hide")) {
    frenchFlag.classList.remove("hide");
    englishFlag.classList.add("hide");
    label.innerText = "Name:";
    submitBtn.innerText = "Log in"
  } else {
    frenchFlag.classList.add("hide");
    englishFlag.classList.remove("hide");
    label.innerText = "Nom:";
    submitBtn.innerText = "Se connecter";
  }
}