MUSICIAN_CREATION = """CREATE TABLE IF NOT EXISTS `Musician`
(
`id` INT NOT NULL PRIMARY KEY, 
`firstname` VARCHAR(45) NOT NULL, 
`surname` VARCHAR(45) NOT NULL, 
`specialization` VARCHAR(45) NOT NULL)
"""

BAND_CREATION = """
CREATE TABLE IF NOT EXISTS `Band`
(
`id_band` INT NOT NULL PRIMARY KEY, 
`bandname` VARCHAR(45) NOT NULL, 
`yearoffoundation` YEAR NOT NULL)
"""

PARTICIPANTS_CREATION = """
CREATE TABLE IF NOT EXISTS `Participants`
( 
`id_musician` INT NOT NULL, 
`id_band` INT NOT NULL,
 FOREIGN KEY (id_musician) REFERENCES Musician (id),
 FOREIGN KEY (id_band) REFERENCES Band (id_band),
 PRIMARY KEY (`id_musician`, `id_band`)
)
"""

PERFORMER_CREATION = """
CREATE TABLE IF NOT EXISTS `Performer`
( 
`id` INT NOT NULL PRIMARY KEY,
`id_musician` INT, 
`id_band` INT,
 FOREIGN KEY (id_musician) REFERENCES Musician (id),
 FOREIGN KEY (id_band) REFERENCES Band (id_band)
)
"""

ALBUM_CREATION = """
CREATE TABLE IF NOT EXISTS `Album`
( 
`id` INT NOT NULL PRIMARY KEY,
`albumname` VARCHAR(90) NOT NULL, 
`year` YEAR NOT NULL,
`genre` VARCHAR(45) NOT NULL,
`id_performer` INT NOT NULL,
 FOREIGN KEY (id_performer) REFERENCES Performer (id)
 )
"""

SONG_CREATION = """
CREATE TABLE IF NOT EXISTS `Song`
( 
`id` INT NOT NULL PRIMARY KEY,
`songname` VARCHAR(90) NOT NULL, 
`id_album` INT NOT NULL,
 FOREIGN KEY (id_album) REFERENCES Album (id)
 )
"""

table_creation_queries = [MUSICIAN_CREATION, BAND_CREATION, PARTICIPANTS_CREATION, PERFORMER_CREATION, ALBUM_CREATION, SONG_CREATION]
