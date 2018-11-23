-- DROP TABLE castor.dbo.College

CREATE TABLE castor.dbo.College (
	Id int NOT NULL,
	Name nvarchar(128) NOT NULL,
	Address nvarchar(255) NOT NULL,
	State nvarchar(2) NOT NULL,
	Zipcode nvarchar(16) NOT NULL,
	AthURL nvarchar(128),
	URL nvarchar(128) NOT NULL,
	NaacId int NOT NULL,
	CONSTRAINT PK_College_1 PRIMARY KEY (Id)
) GO

-- DROP TABLE castor.dbo.Immunization

CREATE TABLE castor.dbo.Immunization (
	Id int NOT NULL IDENTITY(1,1),
	CollegeId int NOT NULL,
	URL nvarchar(512) NOT NULL,
	UrlType nvarchar(4) NOT NULL,
	CONSTRAINT PK_Immunization_1 PRIMARY KEY (Id),
	CONSTRAINT FK_Immunization_1 FOREIGN KEY (CollegeId) REFERENCES castor.dbo.College(Id)
) GO