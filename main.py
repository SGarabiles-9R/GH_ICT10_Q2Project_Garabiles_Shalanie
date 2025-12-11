from js import document, bootstrap
from pyscript import display

# -----------------------
# TAB 2: GWA Calculator
# -----------------------
def getting_info(e):
    name = document.getElementById('input1').value
    section = document.getElementById('input2').value
    document.getElementById('info').innerHTML = ""
    display(f'{name} from {section}', target='info')

def calculating_grades(e):
    eng = float(document.getElementById("subj1").value)
    math = float(document.getElementById("subj2").value)
    sci = float(document.getElementById("subj3").value)
    fili = float(document.getElementById("subj4").value)
    pe = float(document.getElementById("subj5").value)
    ss = float(document.getElementById("subj6").value)
    mus = float(document.getElementById("subj7").value)
    ict = float(document.getElementById("subj8").value)
    tle = float(document.getElementById("subj9").value)
    ve = float(document.getElementById("subj10").value)

    name = document.getElementById('input1').value
    subjects = [eng, math, sci, fili, pe, ss, mus, ict, tle, ve]

    document.getElementById('gwa-output').innerHTML = ""   
    display(f"{name}'s Grades:", target='gwa-output')

    labels = [
        "English", "Mathematics", "Science", "Filipino",
        "Physical Education", "Social Studies",
        "Music", "ICT", "TLE", "Values Education"
    ]

    for label, grade in zip(labels, subjects):
        display(f"{label}: {grade}", target='gwa-output')

    average = sum(subjects) / len(subjects)
    display(f'Your final grade is {average:.2f}', target='gwa-output')

# -----------------------
# TAB 3: Clubs Information
# -----------------------
clubs = {
    "Art Club": {
        "Name of the club": "Art Club",
        "Description": "A club for drawing, painting, and crafts.",
        "Meeting time": "Wednesdays, 3PM",
        "Location": "Room 101, Arts Building",
        "Club Moderator": "Shane Garabiles",
        "Number of members": 25
    },
    "Science Club": {
        "Name of the club": "Science Club",
        "Description": "Experiments, STEM projects, and science competitions.",
        "Meeting time": "Fridays, 4PM",
        "Location": "Lab 3, Science Building",
        "Club Moderator": "Amanda Yao",
        "Number of members": 30
    },
    "Cooking Club": {
        "Name of the club": "Cooking Club",
        "Description": "Cooking, baking, and food preparation.",
        "Meeting time": "Mondays, 2PM",
        "Location": "Kitchen 2, Home Economics Building",
        "Club Moderator": "Dwayne Evangelista",
        "Number of members": 20
    }
}

def show_club(club_name):
    out = document.getElementById("clubs-output")
    club = clubs[club_name]

    html = "<h4>" + club_name + "</h4>"
    html += "<ul class='list-group'>"

    for key, value in club.items():
        html += f"<li class='list-group-item'><b>{key}:</b> {value}</li>"

    html += "</ul>"
    out.innerHTML = html


# Bind buttons RIGHT AWAY (no tab event needed)
document.getElementById("artBtn").addEventListener(
    "click", lambda e: show_club("Art Club")
)
document.getElementById("scienceBtn").addEventListener(
    "click", lambda e: show_club("Science Club")
)
document.getElementById("cookingBtn").addEventListener(
    "click", lambda e: show_club("Cooking Club")
)