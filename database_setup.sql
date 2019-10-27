CREATE TABLE TitleBasics (
	titleId TEXT PRIMARY KEY NOT NULL,
	titleType TEXT,
	primaryTitle TEXT,
	originalTitle TEXT,
	isAdult INT DEFAULT 0,
	startYear INT,
	endYear INT,
	runtimeMinutes INT
);

CREATE TABLE TitleBasicsGenres (
	titleId TEXT NOT NULL REFERENCES TitleBasics (titleId)
		ON DELETE CASCADE ON UPDATE CASCADE,
	genre TEXT NOT NULL
);
