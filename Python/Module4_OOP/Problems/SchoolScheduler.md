---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: School Scheduling Exercise, Difficulty: Easy, Category: Practice Problem
   :keywords: OOP, object oriented programming, object-oriented, practice problem
<!-- #endraw -->

<!-- #region -->
# Designing a School Scheduling System
All schools require some system to keep track of student schedules. The simplest possible means of doing this would be to use a dictionary to store an list of class names using the student's name as the key, but this would make changing class schedules tedious and computationally expensive. Instead, it would be far more effective and efficient for us to store the requisite information in classes designed to store information on students, teachers, class sections and courses. 

To begin, let us consider the structure of this problem. Our goal is to organize and maintain a set of student records containing their `name`, `ID number`, `grade_level`, and a 'class schedule'. The class schedule is a list of 'sections' each of which needs to record the `course` that is being offered, as well as the `teacher`, `room number`, and the `period` in which the class is offered.   

We could accomplish this by storing a list of `section` objects inside of each `student` object, but imagine what would need to happen if a school administrator wanted to change the room number of a class section. Our system would need to check every student's schedule in order to find each instance of the relevant section and make a change to each. Instead, if we simply stored a list of students under each section, a change of this sort would only take a single operation. Similarly, we can organize all sections of the same course under a single `course` object in order to reduce repeated information about the course such as the `department`, `name`, and `course_id`.

### Framework

From a top down persepective, we will aim to organize our `Course`, `Section`, `Teacher`, and `Student` objects like this:

```
|-------------------------------|       |-------------------------------|  
|  Course                       |       |  Course                       |
|-------------------------------|       |-------------------------------|  
|  -----------     -----------  |       |  -----------     -----------  |  
| | Section   |   | Section   | |       | | Section   |   | Section   | | 
| |-----------|   |-----------| |       | |-----------|   |-----------| |
| | Teacher   |   | Teacher   | |       | | Teacher   |   | Teacher   | |
| |           |   |           | |       | |           |   |           | |
| | [Student, |   | [Student, | |       | | [Student, |   | [Student, | |
| |  Student, |...|  Student, | |  ...  | |  Student, |...|  Student, | |
| |  ...,     |   |  ...,     | |       | |  ...,     |   |  ...,     | |
| |  Student] |   |  Student] | |       | |  Student] |   |  Student] | |
|  -----------     -----------  |       |  -----------     -----------  |
|                               |       |                               |
|-------------------------------|       |-------------------------------|
```

### Part 1: Define classes and `__init__` functions

To begin, create the following four classes with the specified parameters, and an `__init__` function to initialize each according to the following function headers:

- `Student`
     - Stores `name`, `id`, and `grade`
 - `Teacher`
     - Stores `name`, `id`, and `dept`
 - `Section`
     - Stores `course_id`, `period`, `teacher` (which holds a `Teacher` object), `room`, and `students` (which holds `[Students]` and defaults to None)
 - `Course`
     - Stores `name`, `dept`, `id`, and `sections`(which stores `[Section]` and defaults to None)

```python
class Student:
    def __init__(self, student_name, student_id, grade_level):
        """ Parameters
            ----------
            student_name: str
                Name of the student
            student_id: int
                Unique ID number of the student
            grade_level: int
                Grade level of the student (1-12)
        """
class Teacher:
    def __init__(self, teacher_name, teacher_id, department):
        """ Parameters
            ----------
            teacher_name: str
                Name of the teacher
            teacher_id: int
                Unique ID number of the teacher
            department: str
                Name of the teacher's department
        """
class Section:
    def __init__(self, course_id, period_num, room_num, teacher, student_list = None):
        """ Parameters
            ----------
            course_id: int
                The course_id associated with this section's Course object
            period_num: int
                Number of the period in which this section is offered (1-6)
            room_num: int
                The number of the room
            teacher: Teacher
                The object representing the teacher leading the section
            student_list: Iterable[Student]
                Iterable of Student objects who are enrolled in this Section
                (defaults to None)
        """   
class Course:
    def __init__(self, course_name, course_id, department, section_list = None):
        """ Parameters
            ----------
            course_name: str
                Name of the course
            course_id: int
                Unique ID number of the course
            department: str
                Department in which the course is offered
            section_list: Iterable[Section]
                Iterable of Section objects offered for the Course
                (defaults to None)
        """
```


 
<!-- #endregion -->

### Part 2: Define `__eq__` functions for each  class

In the next section we will need to compare objects to one another in order to remove them from a list using the `remove()` function or to check equality in later functions. In Python, objects are compared using the special method `__eq__`, which returns `True` if two objects are equal by any definition we choose to use, and `False` otherwise.

Add a function with the header `__eq__(self, other)` to all classes, and find a way to compare them as described above. 

*[Hint: For many (but not all) of the classes, there is an easily accessible unique identifier.]*


<!-- #region -->
### Part 3: Basic Class Methods

Next, we want to be able to add and remove items from the lists we defined in the course and section classes, as well as run a couple of brief utility functions to check a property of the lists that we create. Add the following functions to the indicated classes:

*[Note: add_section creates a new Section object, while add_student adds an already existing Student object. This is because anytime a user of this system creates a Section, it should be added automatically to the list of secions for that course, but Student objects persist and can be added to several sections, so it does not make sense to create a student object in add_student]*

**Course**

```python
def add_section(self, period, room, teacher):
    """ Creates a section and adds it to the sections list
        
        Parameters
        ----------
        period: int
            period of the section to add (1-6)
        room: int
            The number of the room
        teacher: Teacher
            The object representing the teacher leading this section 
    """

def remove_section(self, period, room):
    """ Removes a section from the sections list
    
        Parameters
        ----------
        period: int
            period of the section to remove (1-6)
        room: int
            The number of the room
    """
    
def avg_grade_level(self):
    """ Retruns the average grade level of the students in the section

        Parameters
        ----------
        None

        Returns
        ----------
        float
    """
```
**Section**

```python

def add_student(self, student):
        """ Adds a student to the students list
        
            Parameters
            ----------
            student: Student
                The Student object to add to the list
        """
        
def remove_student(self, student_id):
        """ Removes a student from the student list
        
            Parameters
            ----------
            student_id: int
                ID number of the student to remove
        """
        
def can_run(self):
        """ Returns True if there are between 5 and 25 students in the section 
            and False otherwise
            
            Parameters
            ----------
            None

            Returns
            ----------
            Boolean
        """

```
<!-- #endregion -->

<!-- #region -->
### Part 4: Student Schedules and Class Conflicts

Now that our classes have been created with the specified parameters and functions, we’re ready to start designing the functionality of the platform.

Implement the following functions (along with any helper functions you may choose to use) in a new `Catalog` class which maintains a dictionary of Courses, stored under the department name as its key:

```python
class Catalog:
    def __init__(self, year, course_list):
        """ Parameters
            ----------
            year: int
                The year for this Course Catalog
            course_list: Iterable[Course]
                Iterable of Course objects offered in the given year
        """
    
    def all_sections(self):
        """ Returns a list of all sections from all courses
            
            Parameters
            ----------
            None
                
            Returns
            ----------
            Iterable[Section]
        """
        
    def make_student_schedule(self, student):
        """ Returns a list containing the Section objects for a specific student in order
            of their period (1-6), such that schedule[0] is the students  P1 section,
            and schedule[5] is the students last class. Free periods should be given 
            with a None if a student is not registered in any section for that period.
            
            Parameters
            ----------
            student: Student
                The Student object to generate the schedule for
                
            Returns
            ----------
            Iterable[Section]
                Iterable of Section objects in the student's schedule
        """
    
    def no_class_conflicts(self):
        """ Returns False if there are two sections in the same room at the same period
            or if two sections have the same teacher for the same period, 
            and returns True if no such conflicts exist.
            
            Parameters
            ----------
            None
                
            Returns
            ----------
            Boolean
        """
    
<!-- #endregion -->

<!-- #region -->
## Solution
There are a myriad of equally valid solutions to this problem, but a working example of each class with all functions properly implemented is given below. Since this is certainly not the only way to design these classes, a testing script is also provided below.

```python

class Student:
    # Part 1: Define student class and __init__()
    def __init__(self, student_name, student_id, grade_level):
        """ Parameters
            ----------
            student_name: str
                Name of the student
            student_id: int
                Unique ID number of the student
            grade_level: int
                Grade level of the student (1-12)
        """
        self.name = student_name
        self.id = student_id
        self.grade = grade_level

    # Part 2: Implement an __eq__ method for all classes
    def __eq__(self, other):
        return self.id == other.id


class Teacher:
    # Part 1: Define teacher class and __init__()
    def __init__(self, teacher_name, teacher_id, department):
        """ Parameters
            ----------
            teacher_name: str
                Name of the teacher
            teacher_id: int
                Unique ID number of the teacher
            department: str
                Name of the teacher's department
        """
        self.name = teacher_name
        self.id = teacher_id
        self.dept = department

    # Part 2: Implement an __eq__ method for all classes
    def __eq__(self, other):
        return self.id == other.id


class Course:
    # Part 1: Define Course class and __init__()
    def __init__(self, course_name, course_id, department, section_list=None):
        """ Parameters
            ----------
            course_name: str
                Name of the course
            course_id: int
                Unique ID number of the course
            department: str
                Department in which the course is offered
            section_list: Iterable[Section]
                Iterable of Section objects offered for the Course
                (defaults to None)
        """

        self.name = course_name
        self.id = course_id
        self.dept = department
        self.sections = None

        if section_list is None:
            self.sections = []
        else:
            self.sections = section_list
            
    # Part 2, implement an __eq__ method for all classes
    def __eq__(self, other):
        return (self.id == other.id)
    
    # Part 3: Implement addSection, removeSection, and avg_grade_level
    def add_section(self, period, room, teacher):
        """ Creates a section and adds it to the sections list
            Parameters
            ----------
            period: int
                period of the section to add (1-6)
            room: int
                The number of the room
            teacher: Teacher
                The object representing the teacher leading this section
        """
        new_section = Section(self.id, period, room, teacher)
        self.sections.append(new_section)

    def remove_section(self, period, room):
        """ Removes a section from the sections list
            Parameters
            ----------
            period: int
                period of the section to remove (1-6)
            room: int
                The number of the room
        """
        for sec in self.sections:
            if sec.period == period:
                if sec.room == room:
                    self.sections.remove(sec)

    def avg_grade_level(self):
        """ Retruns the average grade level of the students in the section
            Parameters
            ----------
            None

            Returns
            ----------
            float
        """
        total_grades = 0
        num_students = 0
        for sec in self.sections:
            num_students += len(sec.students)
            for student in sec.students:
                total_grades += student.grade
        return total_grades / num_students


class Section:
    # Part 1: Define Section class and __init__()
    def __init__(self, course_id, period_num, room_num, teacher, student_list=None):
        """ Parameters
            ----------
            course_id: int
                The course_id associated with this section's Course object
            period_num: int
                Number of the period in which this section is offered (1-6)
            room_num: int
                The number of the room
            teacher: Teacher
                The object representing the teacher leading the section
            student_list: Iterable[Student]
                Iterable of Student objects who are enrolled in this Section
                (defaults to None)
        """
        self.course_id = course_id
        self.teacher = teacher
        self.period = period_num
        self.room = room_num

        if student_list is None:
            self.students = []
        else:
            self.students = student_list

    # Part 2: Implement an __eq__ method for all classes
    def __eq__(self, other):
        return (self.course == other.course) and (self.period == other.period)

    # Part 3: Implement addStudent, removeStudent, and can_run
    def add_student(self, student):
        """ Adds a student to the students list
            Parameters
            ----------
            student: Student
                The Student object to add to the list
        """
        self.students.append(student)

    def remove_student(self, student_id):
        """ Removes a student from the student list
            Parameters
            ----------
            student_id: int
                ID number of the student to remove
        """
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)

    def can_run(self):
        """ Returns True if there are between 5 and 25 students in the section
            and False otherwise
            Parameters
            ----------
            None

            Returns
            ----------
            Boolean
        """
        return 5 < len(self.students) < 25


# Part 4: Implement Catalog class with the ability to check that there are
#         no class conflicts, and the ability to make student schedules
class Catalog:
    def __init__(self, year, course_list):
        """ Parameters
            ----------
            year: int
                The year for this Course Catalog
            course_list: Iterable[Course]
                Iterable of Course objects offered in the given year
        """
        self.year = year
        self.courses = course_list

    def all_sections(self):
        """ Returns a list of all sections from all courses

            Parameters
            ----------
            None

            Returns
            ----------
            Iterable[Section]
        """
        sections = []
        for course in self.courses:
            sections.extend(course.sections)
        return sections

    def no_class_conflicts(self):
        """ Returns False if there are two sections in the same room at the same period
            or if two sections have the same teacher for the same period,
            and returns True if no such conflicts exist.

            Parameters
            ----------
            None

            Returns
            ----------
            Boolean
        """
        all_sections = self.all_sections()
        for i in range(len(all_sections)):
            # get relevant data from current section
            sec = all_sections[i]
            room = sec.room
            teacher = sec.teacher
            period = sec.period

            # check for room conflicts and teacher conflicts with a nested loop
            for j in range(i + 1, len(all_sections)):
                other = all_sections[j]
                if other.period == period:
                    if (other.room == room) or (other.teacher == teacher):
                        return False

        # if no conflicts found, return true
        return True

    def make_student_schedule(self, student):
        """ Returns a list containing the Section objects for a specific student in order
            of their period (1-6), such that schedule[0] is the students  P1 section,
            and schedule[5] is the students last class. Free periods should be given
            with a None if a student is not registered in any section for that period.

            Parameters
            ----------
            student: Student
                The Student object to generate the schedule for

            Returns
            ----------
            Iterable[Section]
                Iterable of Section objects in the student's schedule
        """
        student_schedule = [None, None, None, None, None, None]

        for sec in self.all_sections():
            if student in sec.students:
                student_schedule[sec.period - 1] = sec

        return student_schedule

```
<!-- #endregion -->

<!-- #region -->
## Testing 
In order to test using the following script, make sure that your instance variables have the same names as above, or otherwise make sure to edit the testing script to use your instance variable names.

Copy the code below into the same file that contains your class definitions and run the program to test!

```python
import random

# given course_id, return course name or None if not in course list
def lookup_course(self, course_id):
    for course in self.courses:
        if course.id == course_id:
            return course.name
    return None

courses = {
    "Computer Science": Course("AP Computer Science A", 20300, "Computer Science"),
    "Math": Course("AP Calculus BC", 30200, "Math"),
    "English": Course("English 3", 30100, "English"),
    "History": Course("World History", 20100, "History"),
    "Science": Course("Special Topics in Physics", 40100, "Science"),
    "Foreign Languages": Course("AP Spanish", 30300, "Foreign Languages"),
}


students = [
    Student("Andy", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Bella", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Correy", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Dante", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Elija", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Fatima", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Garry", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Hyder", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Imani", random.randint(10000, 99999), random.randint(9, 12)),
    Student("Justin", random.randint(10000, 99999), random.randint(9, 12)),
]

teachers = [
    Teacher("Mr. Anderson", random.randint(1000, 9999), "Computer Science"),
    Teacher("Ms. Barker", random.randint(1000, 9999), "Science"),
    Teacher("Mr. Calary", random.randint(1000, 9999), "History"),
    Teacher("Ms. Dutton", random.randint(1000, 9999), "Math"),
    Teacher("Mx. Ebbra", random.randint(1000, 9999), "English"),
    Teacher("Mr. Farro", random.randint(1000, 9999), "Foreign Languages"),
]

rooms = [102, 104, 107, 203, 205, 208]

for i in range(len(teachers)):
    teacher = teachers[i]
    course = courses.get(teacher.dept)
    course.add_section(1, rooms[i % 6], teacher)
    course.add_section(2, rooms[(i + 1) % 6], teacher)
    course.add_section(3, rooms[i % 6], teacher)
    course.add_section(4, rooms[(i + 1) % 6], teacher)
    course.add_section(5, rooms[i % 6], teacher)
    course.add_section(6, rooms[(i + 1) % 6], teacher)

catalog2021 = Catalog(2021, list(courses.values()))
print("Testing no_class_conflicts() [should be 'True'] - ")
print("No Conflics: " + str(catalog2021.no_class_conflicts()) + "\n")

print("Adding Conflicting Section...")
catalog2021.courses[0].add_section(2, 107, teachers[0])

print("\nTesting no_class_conflicts() [should be 'False'] - ")
print("No Conflics: " + str(catalog2021.no_class_conflicts()) + "\n")

print("\nTesting makeStudentSchedule()-\n")

# creating random student schedules to test
for student in students:
    secs = catalog2021.all_sections()
    schedule = [None, None, None, None, None, None]
    for p in range(6):
        section = secs[random.randint(0, len(secs) - 1)]
        if schedule[section.period - 1] is None:
            section.add_student(student)
            schedule[section.period - 1] = section

    # checking if each student is correctly scheduled
    student_sched = catalog2021.make_student_schedule(student)
    classes_enrolled = list(
        catalog2021.lookup_course(section.course_id)
        for section in student_sched
        if (section is not None)
    )
    print("\nName: " + student.name + "\nClasses Enrolled: ", classes_enrolled)
    print("\nComparing...\nMatching: ", (schedule == student_sched))
```
<!-- #endregion -->

```python

```
