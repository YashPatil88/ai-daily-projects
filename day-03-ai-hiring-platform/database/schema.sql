CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, role TEXT);
CREATE TABLE interviews (id INTEGER PRIMARY KEY, role TEXT, candidate_id INTEGER);
CREATE TABLE results (id INTEGER PRIMARY KEY, score INTEGER, feedback TEXT, interview_id INTEGER);