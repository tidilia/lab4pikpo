create table source_files (
	id integer PRIMARY KEY autoincrement, 
	filename varchar(255) NOT NULL, 
	processed datetime
);

create table processed_data (
	id integer PRIMARY KEY autoincrement,  
	category varchar(255) NOT NULL,
	predmet varchar(255) NOT NULL,
	oborot integer NOT NULL,
	availibility varchar(255) NOT NULL,
	source_file integer NOT NULL,
	CONSTRAINT fk_source_files 
	FOREIGN KEY (data_source) 
	REFERENCES source_files(id) 
	ON DELETE CASCADE
);