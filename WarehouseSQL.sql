--create database UniversityWarehouse collate Latin1_General_CI_AS;
--go


use UniversityWarehouse
go

create table Major(
	ID_Major integer identity(1,1) primary key,
	MajorName varchar(50) not null,
	DegreeName varchar(9) not null,
	Faculty varchar(50)
)
go

create table Course(
	ID_Course integer identity(1,1) primary key,
	CourseName varchar(50) not null,
	Semester numeric,
	ECTS numeric not null,
	IsActive bit not null
)
go

create table Teacher(
	ID_Teacher integer identity(1,1) primary key,
	NameAndSurname varchar(50) not null,
	AcademicTitle varchar(9),
	IsCurrent bit not null,
	SupervisorID integer foreign key references Teacher
)
go

create table Student(
	ID_Student integer identity(1,1) primary key,
	NameAndSurname varchar(50) not null,	
	City varchar(40),
	MissingECTS numeric not null,
	IsActive bit not null,
	"Status" varchar(10) not null
)
go

create table StartDate(
	ID_StartDate integer identity(1,1) primary key,
	"Year" numeric not null,
	Season varchar(6) not null
)
go

create table Junk(
	ID_Junk integer primary key,
	TeachingType varchar(7) not null
)
go

create table Teaching(
	ID_Course integer foreign key references Course,
	ID_Student integer foreign key references Student,
	ID_Teacher integer foreign key references Teacher,
	ID_StartDate integer foreign key references StartDate,
	ID_Junk integer foreign key references Junk,
	Grade numeric not null,
	Completed bit,
	Points numeric
)
go



create table Research(
	ID_Research integer identity(1,1) primary key,
	Topic varchar(50) not null,
	"Year" numeric not null,
	Season varchar(6) not null
)
go

create table Syllabus(
	ID_Course integer foreign key references Course,
	ID_Major integer foreign key references Major
)
go

create table Studying(
	ID_Student integer foreign key references Student,
	ID_Major integer foreign key references Major,
	Graduated bit not null,
	FirstChoice bit,
	StartingYear numeric not null
)
go

create table Authorship(
	ID_Teacher integer foreign key references Teacher,
	ID_Research integer foreign key references Research
)
go




