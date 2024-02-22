
use University
go

create table Major(
	MajorID varchar(7) primary key,
	MajorName varchar(50) not null,
	DegreeName varchar(9) not null,
	StartDate date not null,
	Faculty varchar(50)
)

go

create table Course(
	CourseID varchar(20) primary key,
	CourseName varchar(50) not null,
	Semester integer,
	ECTS integer not null,
	FK_Major varchar(7) foreign key references Major
)
go


create table Teacher(
	TeacherID varchar(8) primary key,
	"Name" varchar(20) not null,
	Surname varchar(30) not null,
	AcademicTitle varchar(9),
	FK_TeacherID varchar(8) foreign key references Teacher
)
go

create table Student(
	StudentID varchar(8) primary key,
	"Name" varchar(20) not null,	
	Surname varchar(30) not null,
	City varchar(40),
	MissingECTS numeric not null,
	FK_Major varchar(7) foreign key references Major
)
go

create table Teaching(
	FK_Course varchar(20) foreign key references Course,
	FK_Student varchar(8) foreign key references Student,
	FK_Teacher varchar(8) foreign key references Teacher,
	"Hours" datetime,
	Grade numeric not null,
	Completed bit,
	Points integer,
	"Type" varchar(10),
	primary key ("FK_Course", "FK_Student","FK_Teacher")
)
go

create table Research(
	ResearchID varchar(8) primary key,
	Topic varchar(50) not null,
	DateOfStart datetime not null,
	DateOfEnding datetime,
	"Status" varchar(9),
	FK_TeacherID varchar(8) foreign key references Teacher	
)
go

CREATE TABLE ConductedON(
	FK_MajorID varchar(7) foreign key references Major,
	FK_ResearchNumber varchar(8) foreign key references Research
)
go

