import matplotlib.pyplot as plt
import numpy as np
#Sample data distribution
data = 
[
    {"age": 22, "gender": "Male"},
    {"age": 11, "gender": "Female"},
    {"age": 35, "gender": "Male"},
    {"age": 3, "gender": "Female"},
    {"age": 52, "gender": "Female"},
    {"age": 29, "gender": "Male"},
    {"age": 17, "gender": "Female"},
    {"age": 19, "gender": "Male"},
    {"age": 84, "gender": "Female"},
    {"age": 45, "gender": "Male"},
    {"age": 91, "gender": "Male"},
    {"age": 6, "gender": "Female"},
    {"age": 24, "gender": "Male"},
    {"age": 15, "gender": "Female"},
    {"age": 70, "gender": "Male"},
    {"age": 22, "gender": "Female"},
    {"age": 13, "gender": "Male"},
    {"age": 25, "gender": "Female"}
]

#Grouping the ages
age_groups = {"0-18": 0, "19-50": 0, "50+": 0}
age_groups_male = {"0-18": 0, "19-50": 0, "50+": 0}
age_groups_female = {"0-18": 0, "19-50": 0, "50+": 0}


for person in data:
    if person['age'] <= 18:
        group = "0-18"
    elif person['age'] <= 50:
        group = "19-50"
    else:
        group = "50+"

    age_groups[group] += 1
    if person['gender'] == "Male":
        age_groups_male[group] += 1
    else:
        age_groups_female[group] += 1


categories = ["0-18", "19-50", "50+"]
male_counts = [age_groups_male[cat] for cat in categories]
female_counts = [age_groups_female[cat] for cat in categories]

plt.figure(figsize=(8, 6))
bar_width = 0.5
indices = np.arange(len(categories))

plt.bar(indices, male_counts, bar_width, label='Male', color='skyblue', edgecolor='black')
plt.bar(indices, female_counts, bar_width, bottom=male_counts, label='Female', color='lightpink', edgecolor='black')

#title 
plt.title('Age Group Distribution by Gender', fontsize=15)
plt.xlabel('Age Groups', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(indices, categories)
plt.legend()

plt.show()


