class Student:
    def __init__(self, name, quiz, hw, project):
        self.name = name
        self.quiz = float(quiz)
        self.hw = float(hw)
        self.project = float(project)
    def get_name(self):
        return self.name
    def score(self):
        return (self.quiz + self.hw + self.project) / 3.0
def main():
    students = []
    students.append(Student("Mike", 70, 60, 80))
    students.append(Student("Rose", 50, 65, 90))
    students.append(Student("Michele", 60, 50, 65+10))
    students.append(Student("Sofia", 80, 65-10,  80))
    # process subsequent lines of the file
    highest = students[0]
    for i in range(1, len(students)):
        if students[i].score() > highest.score():
            highest = students[i]
    print(highest.get_name())
    print(int(highest.score()))
main()

