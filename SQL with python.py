#!/usr/bin/env python
# coding: utf-8

# 

# In[3]:


import psycopg2

class DatabaseOperations():
    def __init__(self):
        self.connection = psycopg2.connect(host='localhost', database="institute", user='postgres', password='2333')
        print("The connection established")
        self.cursor = self.connection.cursor()

    def create_tables(self):
        try:
            # Drop tables if they exist
            self.cursor.execute("DROP TABLE IF EXISTS Courses")
            self.cursor.execute("DROP TABLE IF EXISTS Specialization")

            # Create Specialization table with constraints
            self.cursor.execute("CREATE TABLE Specialization (specialization_code INT PRIMARY KEY, specialization_name VARCHAR(20) UNIQUE)")

            # Create Courses table with constraints
            self.cursor.execute("CREATE TABLE Courses (course_code INT PRIMARY KEY, course_name VARCHAR(50), specialization_code INT, FOREIGN KEY (specialization_code) REFERENCES Specialization(specialization_code))")

            self.connection.commit()
            print("Tables created successfully.")
        except psycopg2.Error as e:
            print("Error creating tables:", e)

    def insert_records(self):
        try:
            # Insert records into Specialization table
            specialization_records = [
                (1, 'MSc(DSSA)'),
                (2, 'MSc(CA)'),
            ]
            self.cursor.executemany("INSERT INTO Specialization VALUES (%s, %s)", specialization_records)

            # Insert records into Courses table
            courses_records = [
                (101, 'Python for Data Science', 1),
                (102, 'Machine Learning', 1),
                (103, 'Big Data Analytics', 1),
                (201, 'Advanced Algorithms', 2),
                (202, 'Database Management', 2),
                (203, 'Cloud Computing', 2),
            ]
            self.cursor.executemany("INSERT INTO Courses VALUES (%s, %s, %s)", courses_records)

            self.connection.commit()
            print("Records inserted successfully.")
        except psycopg2.Error as e:
            print("Error inserting records:", e)

    def display_specializations_and_courses(self):
        try:
            # Query to select specialization names and corresponding courses
            select_query = '''
            SELECT s.specialization_name, c.course_name
            FROM Specialization s
            JOIN Courses c ON s.specialization_code = c.specialization_code
            ORDER BY s.specialization_name
            '''
            self.cursor.execute(select_query)
            specialization_courses = self.cursor.fetchall()

            print("Specialization Name\tCourses Offered")
            for specialization, course in specialization_courses:
                print(f"{specialization}\t\t{course}")
        except psycopg2.Error as e:
            print("Error fetching data:", e)

if __name__ == "__main__":
    data = DatabaseOperations()
    data.create_tables()
    data.insert_records()
    data.display_specializations_and_courses()


# In[ ]:




