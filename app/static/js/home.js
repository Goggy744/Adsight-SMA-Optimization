const tyMessage = document.getElementById("tyMessage");
const frenchFlag = document.getElementById("french-flag");
const englishFlag = document.getElementById("english-flag");
const frenchDescription = document.getElementById("french-description");
const englishDescription = document.getElementById("english-description");
const welcomeMessage = document.getElementById("welcome-message");
const startBtn = document.getElementById("start-btn");

function languageManagement() {
  if (frenchFlag.classList.contains("hide")) {
    frenchFlag.classList.remove("hide");
    frenchDescription.classList.add("hide");
    englishFlag.classList.add("hide");
    englishDescription.classList.remove("hide");
    welcomeMessage.innerText = "Welcome to Adsight Experiment!";
    startBtn.innerText = "Start";
    tyMessage.innerText = "Thank you once again for your participation. Your contribution is essential to help us better understand how the visual elements of ads influence user behavior on social networks.If you're ready to get started, please click on start.";
  } else {
    frenchFlag.classList.add("hide");
    frenchDescription.classList.remove("hide");
    englishFlag.classList.remove("hide");
    englishDescription.classList.add("hide");
    welcomeMessage.innerText = "Bienvenue sur l'expérience Adsight";
    startBtn.innerText = "Commencer";
    tyMessage = "Nous vous remercions encore une fois pour votre participation. Votre contribution est essentielle pour nous aider à mieux comprendre comment les éléments visuels des publicités influencent le comportement des utilisateurs sur les réseaux sociaux. Si vous êtes prêt à commencer, veuillez cliquer sur commencer.";
  }
}



