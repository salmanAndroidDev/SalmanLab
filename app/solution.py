def getBMI(height, weight):
    return weight / ((height/100) ** 2)
    

def process(path):
    # path = """179 73.8 ATHLETE
    #     179 71.8 ATHLETE
    #     172 71.3 ATHLETE
    #     151 85.0 NORMAL
    #     192 91.8 NORMAL"""

    athletes = []
    athletes_average_bmi = 0.000
    normal_people = []
    normal_average_bmi = 0.000

    counter_for_athletes = 0
    counter_for_normals = 0

    text = []
    text.extend(path.split('\n'))
    
    for word in text:
        height, weight, mode = word.split()
        height = int(height)
        weight = float(weight)
        BMI = getBMI(height, weight)

        if mode == 'ATHLETE':
            counter_for_athletes += 1
            athletes.append((height, weight, BMI))
            athletes_average_bmi += BMI  
        else:
            counter_for_normals += 1
            normal_people.append((height, weight, BMI))
            normal_average_bmi += BMI

    if counter_for_athletes > 0:
        athletes_average_bmi /= counter_for_athletes

    if counter_for_normals > 0:
        normal_average_bmi /= counter_for_normals    

    athletes = "athletes = {}".format(athletes)
    athletes_average_bmi = 'athletes_average_bmi = {}'.format(athletes_average_bmi)
    normal_people = "normalPeople = {}".format(normal_people)    
    normal_average_bmi = 'normal_average_bmi = {}'.format(normal_average_bmi)
    
    return athletes , athletes_average_bmi , normal_people, normal_average_bmi