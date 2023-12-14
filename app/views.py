from flask import Blueprint, render_template, redirect, url_for, request, jsonify, json
import time
from .data import *
from random import shuffle

#Create the views Blueprint
views = Blueprint('views', __name__, url_prefix="/")


#description for home page
descriptionItemsFrench = {
  1: ["Titre de l'Expérience : Analyse du Comportement Visuel dans un Feed Instagram Simulé",
      "Cher participant, nous vous souhaitons la bienvenue à notre expérience de recherche sur le comportement visuel dans un feed Instagram simulé. Votre participation est précieuse et nous vous remercions de vous joindre à nous pour cette étude."
      ],
  2: ["Objectif de l'Expérience :",
      "L'objectif de cette expérience est de comprendre comment différents éléments visuels et de conception affectent le comportement visuel des utilisateurs lorsqu'ils parcourent un feed Instagram simulé. En tant que participant, vous jouerez un rôle essentiel dans cette recherche."
      ],
  3: ["Déroulement de l'Expérience :",
      "Vous serez invité à parcourir les publications dans le feed. Votre tâche consistera à interagir avec les publications en cliquant sur celles qui vous intéressent, comme si vous naviguiez réellement sur Instagram.Nous utiliserons un logiciel de suivi oculaire pour collecter des données sur vos mouvements oculaires pendant que vous parcourrez le feed. Cela nous aidera à comprendre où vous portez votre attention et comment vous interagissez avec les publications."
      ],
  4: ["Confidentialité :",
      "Veuillez noter que toutes les données collectées resteront confidentielles. Votre participation sera anonyme, et les données seront utilisées uniquement à des fins de recherche."
      ],
  5: ["Durée de l'Expérience :",
      "L'expérience devrait prendre environ [indiquez la durée approximative] minutes."
      ]
}
descriptionItemsEnglish = {
  1: ["Title of the Experiment: Analysis of Visual Behavior in a Simulated Instagram Feed",
      "Dear participant, we welcome you to our research experiment on visual behavior in a simulated Instagram feed. Your participation is valuable and we thank you for joining us in this study."
      ],
  2: ["Aim of the experiment:",
      "The aim of this experiment is to understand how different visual and design elements affect users' visual behavior when browsing a simulated Instagram feed. As a participant, you will play a key role in this research."
      ],
  3: ["How the Experience unfolds:",
      "You'll be invited to browse the publications in the feed. Your task will be to interact with the publications by clicking on the ones that interest you, as if you were actually browsing Instagram. We'll use eye-tracking software to collect data on your eye movements as you browse the feed. This will help us understand where you focus your attention and how you interact with publications."
      ],
  4: ["Privacy policy:",
      "Please note that all data collected will remain confidential. Your participation will be anonymous, and the data will be used for research purposes only."
      ],
  5: ["Duration of experience:",
      "The experiment should take about [give approximate time] minutes."
      ]
}

@views.route("/", methods = ["POST", "GET"])
def logUser():
    if request.method == "POST":
        userId = f"user{getUserId()}"
        createExpTimestamp(userId)
        logInTime = time.time()
        addEvent("LOGIN", logInTime, userId)
        
        return redirect(url_for("views.home",userId = userId))       
    else:
        return render_template("logUser.html")


@views.route("/description-<userId>", methods=["GET", "POST"])
def home(userId):
    if userId:
        if request.method == "POST":
            experienceStartTime = time.time() + 10
            addEvent("ExpStart", experienceStartTime, userId)
            return redirect(url_for("views.clone", userId = userId))
        else:
            return render_template("home.html",
                                    descriptionItemsFrench=descriptionItemsFrench,
                                    descriptionItemsEnglish=descriptionItemsEnglish) 
    else:
        return render_template("logUser.html")
    

@views.route("/adsight-<userId>", methods=['GET', 'POST'])
def clone(userId):
    if request.method == 'POST':
        addEvent('ExpEnd', time.time(), userId)
        return redirect(url_for('views.logUser'))
    else:
        jsonFile = open('app/fake-post.json')
        fake_posts = json.load(jsonFile)
        jsonFile.close()
        jsonFile = open('app/fake-ads.json')
        fake_ads = json.load(jsonFile)
        jsonFile.close()
        
        fake_articles = fake_posts['posts'] + fake_ads['advertisements']
        shuffle(fake_articles)
        
        return render_template("clone.html", fake_articles = fake_articles)


@views.route('/process-data', methods = ['POST'])
def processData():
    data = request.get_json()
    if type(data) == list:
        fname = f'exp{getUserId() - 1}'
        createExpInfo(fname, data)
    if type(data) == dict:    
        eventName = data['eventName']
        articleIndex = data['articleIndex']
        userId = data['userId']
        addEvent(f"{eventName}{articleIndex}", time.time(), userId)
    return jsonify({})


