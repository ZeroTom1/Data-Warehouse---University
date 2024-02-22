use University
delete from Teaching
delete from ConductedON
delete from Course
delete from Research
delete from Teacher
delete from Student
delete from Major


BULK INSERT Major FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\major_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT Course FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\course_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT Research FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\research_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT Teacher FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\teacher_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT Student FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\student_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT Teaching FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\teaching_data.bulk' WITH (FIELDTERMINATOR=',')
BULK INSERT ConductedON FROM 'C:\Users\tombe\PycharmProjects\pythonProject1\conductedON.bulk' WITH (FIELDTERMINATOR=',')