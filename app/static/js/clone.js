let timerSection = document.getElementById('timer-section');
let counter = document.getElementById('counter-id');
let expSection = document.getElementById('insta-clone-id');


function timer(counter) {
  counter.innerText = parseInt(counter.innerText) - 1
}

function startExp(expSection, timerSection) {
  timerSection.classList.add('hide');
  expSection.classList.remove('hide');
}

//Counter at the start of the page
let timerInterval = setInterval( () => timer(counter), 1000);
setTimeout( () => {clearInterval(timerInterval); startExp(expSection, timerSection);}, 1000)

//Get userId inside the url of the page
const userId = document.URL.split('/').slice(-1)[0].split('-').slice(-1)[0];

//Send data
function sendData(data_dict) {
  //Create the request
  $.ajax({
    url: '/process-data',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(data_dict),
    success: function(){
      console.log('success');
    },
    error: function(){
      console.log('error');
    }
  });
}
//Like function
function like(btn){
  const childList = [btn.children[0], btn.children[1]]

  //Unlike
  if (childList[0].classList.contains('hide')) {
    childList[0].classList.remove('hide');
    childList[1].classList.add('hide');
  //Like
  } else {
    childList[1].classList.remove('hide');
    childList[0].classList.add('hide');
    //Send data to flask
    sendData({
      'eventName': 'Like-',
      'articleIndex': articleIndex,
      'userId': userId
    });
  }
}
function callToAction(btn) {
  btn.style.background = 'mediumpurple';
  btn.style.color = 'white';
  btn.innerText = 'Booked!';
  sendData({
    'eventName': 'CTA-',
    'articleIndex': articleIndex,
    'userId': userId
  });
}
//Scroll behavior
const articles = document.getElementsByTagName('article');
let post_height = 799;
let articles_height = new Array;
articles_height.push(0);
let articleIndex = 1;

for (let i = 1; i <= articles.length; i++){
  articles_height.push(post_height * i)
}

document.addEventListener('scroll', (event) => {
  let new_array = articles_height.copyWithin();
  new_array.push(scrollY);
  new_array.sort((a,b) => a-b);
  articleIndex = new_array.indexOf(scrollY);
  new_array.splice(articleIndex, 1);


  //Send data to flask
  sendData({
            'eventName':  'ScrollToArticle-',
            'articleIndex': articleIndex, 
            'userId': userId
          });
})

//Send page layout onload
setTimeout( () => {
  console.log('loaded');
  // Full height, including the scroll part
  const fullHeight = Math.max(
    document.body.scrollHeight,
    document.documentElement.scrollHeight,
    document.body.offsetHeight,
    document.documentElement.offsetHeight,
    document.body.clientHeight,
    document.documentElement.clientHeight
  );
  // Full width, including the scroll part
  const fullWidth = Math.max(
    document.body.scrollWidth,
    document.documentElement.scrollWidth,
    document.body.offsetWidth,
    document.documentElement.offsetWidth,
    document.body.clientWidth,
    document.documentElement.clientWidth
  );

  data = []
  data.push({id: userId})
  data.push({document: `${fullWidth}x${fullHeight}`})
  data.push({articleSize: '470x'+post_height })
  data.push({articleLayout:{}})
  let i = 1;
  
  for (let article of articles) {
    data[data.length-1]['articleLayout'][i] = article.className;
    i++;
  }
  $.ajax({
    url: '/process-data',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(data),
    success: function(){
      console.log('success');
    },
    error: function(){
      console.log('error');
    }
  })
}, 2000);




