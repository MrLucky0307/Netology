CREATE TABLE IF NOT EXISTS genre (
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS performer (
	performer_id SERIAL PRIMARY KEY,
	name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	graduation_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS track (
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	leigth INTEGER NOT NULL,
	album_id INTEGER NOT NULL REFERENCES album(album_id)
);

CREATE TABLE IF NOT EXISTS collection (
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	graduation_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS performer_album (
	performer_album_id SERIAL PRIMARY KEY,
	performer_id INTEGER NOT NULL REFERENCES performer_id(performer),
	album_id INTEGER NOT NULL REFERENCES album_id(album)
);

CREATE TABLE IF NOT EXISTS genre_performer (
	genre_performer_id SERIAL PRIMARY KEY,
	genre_id INTEGER NOT NULL REFERENCES genre_id(genre),
	performer_id INTEGER NOT NULL REFERENCES performer_id(performer)
);

CREATE TABLE IF NOT EXISTS track_collection (
	track_collection_id SERIAL PRIMARY KEY,
	track_id INTEGER NOT NULL REFERENCES track_id(track),
	collection_id INTEGER NOT NULL REFERENCES collection_id(collection)
);