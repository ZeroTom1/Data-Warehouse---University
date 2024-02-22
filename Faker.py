from datetime import *
from pandas import DataFrame
from faker import Faker
from random import randint
import random
import uuid

fake = Faker()

NrOfTeachers = 500
NrOfResearch = 1500
NrOfStudents = 5000
# Define course names for each major

major_courses = {
    "Mechanical Engineering": ["Thermodynamics", "Fluid Mechanics", "Mechanical Design", "Materials Science",
                               "Structural Mechanics", "Robotics", "Mechatronics", "Advanced Mechanics of Materials",
                               "Finite Element Analysis", "Vibration and Control", "Engineering Optimization"],
    "Electrical Engineering": ["Circuits and Electronics", "Signals and Systems", "Digital Signal Processing",
                               "Power Systems", "Control Systems", "Renewable Energy", "Electromagnetic Theory",
                               "Power Electronics", "Microelectronic Circuits", "Communication Systems",
                               "Computer Networks"],
    "Computer Science": ["Data Structures and Algorithms", "Programming Languages", "Computer Networks",
                         "Operating Systems", "Databases", "Artificial Intelligence", "Computer Graphics",
                         "Web Development", "Human-Computer Interaction", "Data Science", "Software Engineering"],
    "Software Engineering": ["Software Design", "Requirements Engineering", "Software Testing", "Software Quality",
                             "Agile Development", "DevOps", "Software Metrics", "Software Security",
                             "Software Maintenance", "Software Verification and Validation",
                             "Software Configuration Management"],
    "Mathematics": ["Calculus", "Linear Algebra", "Differential Equations", "Topology", "Number Theory",
                    "Complex Analysis", "Real Analysis", "Partial Differential Equations", "Graph Theory",
                    "Number Theory", "Algebraic Geometry"],
    "Statistics": ["Probability Theory", "Statistical Inference", "Regression Analysis", "Experimental Design",
                   "Bayesian Statistics", "Time Series Analysis", "Multivariate Analysis", "Nonparametric Statistics",
                   "Sampling Theory", "Design of Experiments", "Spatial Statistics"],
    "Data Science": ["Data Mining", "Machine Learning", "Big Data Analytics", "Data Visualization", "Deep Learning",
                     "Natural Language Processing", "Data Wrangling", "Data Ethics", "Reinforcement Learning",
                     "Bayesian Networks", "Neural Networks"],
    "Physics": ["Classical Mechanics", "Quantum Mechanics", "Electromagnetism", "Thermodynamics", "Astrophysics",
                "Particle Physics", "Statistical Mechanics", "Optics", "Nuclear Physics", "Solid State Physics",
                "Plasma Physics"],
    "Chemistry": ["Organic Chemistry", "Inorganic Chemistry", "Analytical Chemistry", "Physical Chemistry",
                  "Biochemistry", "Polymer Chemistry", "Environmental Chemistry", "Materials Chemistry",
                  "Computational Chemistry", "Photochemistry", "Quantum Chemistry"],
    "Biology": ["Cell Biology", "Genetics", "Ecology", "Microbiology", "Evolutionary Biology", "Molecular Biology",
                "Neurobiology", "Immunology", "Developmental Biology", "Plant Biology", "Animal Behavior"],
    "Biochemistry": ["Biochemical Reactions", "Metabolism", "Proteins and Enzymes", "Molecular Biology", "Genetics",
                     "Structural Biology", "Bioinformatics", "Immunology", "Pharmacology", "Cancer Biology",
                     "Protein Engineering"],
    "Environmental Science": ["Environmental Monitoring", "Ecotoxicology", "Environmental Management", "Climate Change",
                              "Sustainable Development", "Renewable Energy", "Water Resource Management",
                              "Ecological Modeling", "Air Pollution", "Waste Management", "Environmental Law"],
    "Materials Engineering": ["Materials Science", "Materials Processing", "Nanomaterials", "Biomaterials",
                              "Composite Materials", "Metallurgy", "Electronic Materials",
                              "Mechanical Behavior of Materials", "Advanced Ceramics", "Surface Engineering",
                              "Materials Character"],
    "Geology": ["Mineralogy", "Sedimentology", "Tectonics", "Petrology", "Geochemistry", "Geophysics",
                "Structural Geology", "Geological Mapping", "Volcanology", "Paleontology", "Environmental Geology"],
    "Astronomy": ["Astronomical Observations", "Cosmology", "Astrophysics", "Planetary Science", "Astrobiology",
                  "Gravitational Waves", "Exoplanet Astronomy", "Stellar Evolution", "Galactic Astronomy",
                  "High Energy Astrophysics", "Observational Astronomy"],
    "Neuroscience": ["Neuroanatomy", "Neurophysiology", "Cognitive Neuroscience", "Behavioral Neuroscience",
                     "Neuropsychology", "Neuropharmacology", "Affective Neuroscience", "Developmental Neuroscience",
                     "Computational Neuroscience", "Neuroimaging", "Neuroethics"],
    "Cognitive Science": ["Cognition and Perception", "Language and Thought", "Decision Making",
                          "Artificial Intelligence", "Neuroscience", "Philosophy of Mind", "Emotion and Cognition",
                          "Embodied Cognition", "Social Cognition", "Consciousness", "Neuroeconomics"],
    "Artificial Intelligence": ["Machine Learning", "Natural Language Processing", "Computer Vision", "Robotics",
                                "Expert Systems", "Deep Learning", "Reinforcement Learning",
                                "Probabilistic Graphical Models", "Computer Speech and Language Processing",
                                "Knowledge Representation and Reasoning", "Generative Adversarial Networks"],
    "Robotics": ["Robot Kinematics and Dynamics", "Robot Perception and Control", "Robotics Design and Fabrication",
                 "Human-Robot Interaction", "Mobile Robotics", "Multi-Robot Systems", "Robot Localization and Mapping",
                 "Robotic Vision", "Soft Robotics", "Autonomous Navigation and Control", "Robot Swarm Intelligence"],
    "Cybersecurity": ["Cryptography", "Network Security", "Digital Forensics", "Security Management",
                      "Information Privacy", "Risk Assessment", "Intrusion Detection and Prevention",
                      "Cyber Threat Intelligence", "Cybersecurity Analytics", "Identity and Access Management",
                      "Vulnerability Assessment"],
    "Mathematical Biology": ["Mathematical Modeling in Biology", "Systems Biology", "Biostatistics",
                             "Computational Biology", "Population Biology", "Ecosystem Dynamics", "Bioinformatics",
                             "Mathematical Epidemiology", "Biomechanics", "Theoretical Neuroscience",
                             "Computational Biophysics"],
    "Computer Engineering": ["Digital Systems Design", "Computer Architecture", "Operating Systems", "Databases",
                             "Artificial Intelligence", "Embedded Systems Design", "Computer Networks",
                             "Real-Time Systems", "Computer Graphics", "Computer Security"]
}

additional_courses = ["Entry Calculus", "Entry Algebra", "English", "BHP", "Basics of Physics", "Philosophy"]

# Loop through each major in the major_courses dictionary
for major in major_courses:
    # Add the additional courses to the list of courses for the current major
    major_courses[major] += additional_courses

faculties = [
    "Faculty of Mechanical Engineering",
    "Faculty of Electrical Engineering",
    "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Science", "Faculty of Science", "Faculty of Science", "Faculty of Science", "Faculty of Science",
    "Faculty of Science",
    "Faculty of Geology",
    "Faculty of Science",
    "Faculty of Psychology", "Faculty of Psychology",
    "Faculty of Mathematics, Informatics and Mechanics", "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Mathematics, Informatics and Mechanics", "Faculty of Mathematics, Informatics and Mechanics",
    "Faculty of Electrical Engineering"
]

# Generate fake data for Major table
majors = list(major_courses.keys())
start_years = [2018, 2019, 2020, 2021, 2022]
major_data = []
for year in start_years:
    for i in range(len(majors)):
        major = {
            'MajorID': 'M' + str(i + 1) + str(year),
            'MajorName': majors[i],
            'DegreeName': "Engineer" if "Engineering" in majors[i] else random.choices(
                population=["Bachelor", "Master"],
                weights=[0.6, 0.4]
            )[0],
            'StartDate': str(year) + '-10-01',
            'Faculty': faculties[i]
        }
        major_data.append(major)

# Generate fake data for Course table
course_data = []  ###te kursy nie mają sensu, bo muszą na tych samych kierunkach zawsze być w tym samym semie
for year in start_years:
    if datetime.now().month > 9:
        semesters = (datetime.now().year - year) * 2
    else:
        semesters = ((datetime.now().year - year) * 2) - 1
    if semesters > 7:
        semesters = 7
    for i in range(len(majors)):
        counter = 0
        for j in range(semesters):
            # course_name = major_courses[majors[i]][randint(0, 5)]  # get a random course from major a bit of hard coding
            for k in range(2):
                course_name = major_courses[majors[i]][counter]
                course = {
                    'CourseID': 'C' + str(i + 1) + str(course_name[:3]).upper() + str(year),
                    'CourseName': course_name,
                    'Semester': j + 1,
                    'ECTS': random.randint(1, 8),
                    'FK_Major': 'M' + str(i + 1) + str(year),
                    #                   'CourseBaseName': majors[i]  # Add new field to Course table to indicate base course name
                }
                counter = counter + 1
                course_data.append(course)

# Generate fake data for Teacher table
teacher_data = []

teacher_uuid = [str(uuid.uuid4())[:8] for i in range(NrOfTeachers)]

for i in range(NrOfTeachers):
    education_level = random.choices(['Associate', 'Bachelor', 'Master', 'Doctor'], weights=[0.2, 0.3, 0.3, 0.2], k=1)[
        0]
    teacher = {
        'TeacherID': teacher_uuid[i],
        'Name': fake.first_name(),
        'Surname': fake.last_name(),
        'AcademicTitle': education_level,
        'FK_TeacherID': "NULL" if education_level == 'Associate' else teacher_uuid[random.randint(1, NrOfTeachers - 1)]
        # tu by można było wszystkie przypadki rozpisać
    }
    teacher_data.append(teacher)

# Generate fake data for Research table
research_data = []
for i in range(NrOfResearch):
    research = {
        'ResearchID': str(uuid.uuid4())[:8],
        'Topic': fake.sentence(nb_words=5),
        'DateOfStart': fake.date_between(start_date='-5y', end_date='today'),
        'DateOfEnding': fake.date_between(start_date='-4y', end_date='today'),
        'Status': random.choice(['Ongoing', 'Completed']),
        'FK_TeacherID': teacher_uuid[random.randint(1, NrOfTeachers - 1)]
    }
    research_data.append(research)

# Generate fake data for Student table
students_uuid = [str(uuid.uuid4())[:8] for i in range(NrOfStudents)]

student_data = []
for i in range(NrOfStudents):
    # nomissing - chance of the missingECTS points being 0
    # somemissing - chance of the missingECTS points being 1-12
    # moremissing - chance of the missingECTS points being 13-30
    nomissing = 0.35
    somemissing = 0.4
    moremissing = 0.25

    # Use random.choices() to randomly select a value for MissingECTS based on the weights
    missing_ects = random.choices(
        [0] + list(range(1, 13)) + list(range(13, 31)),
        weights=[nomissing] + [somemissing / 12] * 12 + [moremissing / 18] * 18
    )[0]

    student = {
        'StudentID': students_uuid[i],
        'Name': fake.first_name(),
        'Surname': fake.last_name(),
        'City': fake.city(),
        'MissingECTS': missing_ects,
        'FK_Major': 'M' + str(random.randint(1, len(majors))) + str(random.choice(start_years)),
    }
    student_data.append(student)

# Generate fake data for Excel spreadsheet
Excel_data = []
for student in student_data:
    Math = randint(0, 100)
    Physics = randint(0, 100)
    Polish = randint(0, 100)
    English = randint(0, 100)
    PointsFromRecruitment = Math + Physics + Polish + English
    FirstChoice = student['FK_Major']
    SecondChoice = majors[randint(0, len(majors) - 1)]
    FirstFirst = random.choices([FirstChoice, SecondChoice], weights=[0.7, 0.3])
    StudentRecruitment = {
        'StudentID': student['StudentID'],
        'City': student['City'],
        'A_levels_Math': Math,
        'A_levels_Physics': Physics,
        'A_levels_Polish': Polish,
        'A_levels_English': English,
        'FirstChoice': FirstFirst,
        'SecondChoice': FirstChoice if FirstFirst == SecondChoice else FirstChoice,
        'PointsFromRecruitment': PointsFromRecruitment,
    }
    Excel_data.append(StudentRecruitment)
# Generate fake data for Teaching table
teaching_data = []
for student in student_data:
    for course in course_data:
        if course['FK_Major'][1] == student['FK_Major'][1]:
            hour = random.randint(6, 22)
            teaching_datetime = datetime(2023, 3, 16, hour, 0)
            grade = random.choices([2, 3, 3.5, 4, 4.5, 5], weights=[0.2, 0.35, 0.2, 0.12, 0.08, 0.05])
            points = 0
            if grade[0] == 2:
                points = random.randint(0, 50)
            elif grade[0] == 3:
                points = random.randint(50, 60)
            elif grade[0] == 3.5:
                points = random.randint(61, 70)
            elif grade[0] == 4:
                points = random.randint(70, 80)
            elif grade[0] == 4.5:
                points = random.randint(80, 90)
            elif grade[0] == 5:
                points = random.randint(90, 100)
            teaching = {
                'FK_Course': course['CourseID'],
                'FK_Student': student['StudentID'],
                'FK_Teacher': teacher_uuid[random.randint(1, NrOfTeachers - 1)],
                'Hours': teaching_datetime.strftime("%H:%M"),
                'Grade': grade[0],
                'Completed': random.choice([0, 1]),
                'Points': points,
                'Type': random.choice(['Online', 'Stationary', 'Hybrid'])
            }
            teaching_data.append(teaching)
'''
# Write data to text files
with open('major_data.txt', 'w') as f:
    for major in major_data:
        f.write('\t'.join(str(val) for val in major.values()) + '\n')

with open('course_data.txt', 'w') as f:
    for course in course_data:
        f.write('\t'.join(str(val) for val in course.values()) + '\n')

with open('teacher_data.txt', 'w') as f:
    for teacher in teacher_data:
        f.write('\t'.join(str(val) for val in teacher.values()) + '\n')

with open('research_data.txt', 'w') as f:
    for research in research_data:
        f.write('\t'.join(str(val) for val in research.values()) + '\n')

with open('student_data.txt', 'w') as f:
    for student in student_data:
        f.write('\t'.join(str(val) for val in student.values()) + '\n')

with open('excel_data.txt', 'w') as f:
    for StudentRecruitment in Excel_data:
        f.write('\t'.join(str(val) for val in StudentRecruitment.values()) + '\n')

with open('teaching_data.txt', 'w') as f:
    for teaching in teaching_data:
        f.write('\t'.join(str(val) for val in teaching.values()) + '\n')
'''
# Write data to text files as INSERT STATEMENT

with open('major_data.txt', 'w') as f:
    for major in major_data:
        query = f"INSERT INTO Major VALUES ('{major['MajorID']}', '{major['MajorName']}', '{major['DegreeName']}', '{major['StartDate']}', '{major['Faculty']}');\n"
        f.write(query)

with open('course_data.txt', 'w') as f:
    for course in course_data:
        query = f"INSERT INTO Course VALUES ('{course['CourseID']}', '{course['CourseName']}', '{course['Semester']}', '{course['ECTS']}', '{course['FK_Major']}');\n"
        f.write(query)

with open('teacher_data.txt', 'w') as f:
    for teacher in teacher_data:
        query = f"INSERT INTO Teacher VALUES ('{teacher['TeacherID']}', '{teacher['Name']}', '{teacher['Surname']}', '{teacher['AcademicTitle']}', '{teacher['FK_TeacherID']}');\n"
        f.write(query)

with open('research_data.txt', 'w') as f:
    for research in research_data:
        query = f"INSERT INTO Research VALUES ('{research['ResearchID']}', '{research['Topic']}', '{research['DateOfStart']}', '{research['DateOfEnding']}', '{research['Status']}', '{research['FK_TeacherID']}');\n"
        f.write(query)

with open('student_data.txt', 'w') as f:
    for student in student_data:
        query = f"INSERT INTO Student VALUES ('{student['StudentID']}', '{student['Name']}', '{student['Surname']}', '{student['City']}', '{student['MissingECTS']}', '{student['FK_Major']}');\n"
        f.write(query)

with open('excel_data.txt', 'w') as f:
    for StudentRecruitment in Excel_data:
        f.write('\t'.join(str(val) for val in StudentRecruitment.values()) + '\n')

with open('teaching_data.txt', 'w') as f:
    for teaching in teaching_data:
        query = f"INSERT INTO Teachings VALUES ('{teaching['FK_Course']}', '{teaching['FK_Student']}', '{teaching['FK_Teacher']}', '{teaching['Hours']}', '{teaching['Grade']}', '{teaching['Completed']}', '{teaching['Points']}', '{teaching['Type']}');\n"
        f.write(query)

teacher_list = []
with open("teacher_data.txt", "r") as f:
    for line in f:
        line = line.strip()
        values = line.split("'")[1::2]
        teacher_list.append(values)

teacher_update_list = []
for i in range(len(teacher_list)):
    if i % 13 == 0:
        teacher_update_list.append(teacher_list[i][0])

with open('teacher_data_update.txt', 'w') as f:
    for teacher in teacher_data:
        query = f"UPDATE Teacher set Surname = {fake.last_name()} WHERE TeacherID = {teacher['TeacherID']};\n"
        f.write(query)