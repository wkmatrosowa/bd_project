MUSICIAN_CREATION = """CREATE TABLE IF NOT EXISTS `musician`
(
`id` INT NOT NULL PRIMARY KEY, 
`firstname` VARCHAR(45) NOT NULL, 
`surname` VARCHAR(45) NOT NULL, 
`specialization` VARCHAR(45) NOT NULL)
"""

BAND_CREATION = """
CREATE TABLE IF NOT EXISTS `band`
(
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`bandname` VARCHAR(45) NOT NULL, 
`yearoffoundation` YEAR NOT NULL)
"""

PARTICIPANTS_CREATION = """
CREATE TABLE IF NOT EXISTS `participants`
( 
`id_musician` INT NOT NULL, 
`id_band` INT NOT NULL,
 FOREIGN KEY (id_musician) REFERENCES musician (id),
 FOREIGN KEY (id_band) REFERENCES band (id),
 PRIMARY KEY (`id_musician`, `id_band`)
)
"""

PERFORMER_CREATION = """
CREATE TABLE IF NOT EXISTS `performer`
( 
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`id_musician` INT, 
`id_band` INT,
 UNIQUE KEY (`id_musician`),
 UNIQUE KEY (`id_band`),
 FOREIGN KEY (id_musician) REFERENCES musician (id),
 FOREIGN KEY (id_band) REFERENCES band (id)
)
"""

ALBUM_CREATION = """
CREATE TABLE IF NOT EXISTS `album`
( 
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`albumname` VARCHAR(90) NOT NULL, 
`year` YEAR NOT NULL,
`genre` VARCHAR(45) NOT NULL,
`id_performer` INT NOT NULL,
 FOREIGN KEY (id_performer) REFERENCES performer (id)
 )
"""

SONG_CREATION = """
CREATE TABLE IF NOT EXISTS `song`
( 
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`songname` VARCHAR(90) NOT NULL, 
`id_album` INT NOT NULL,
 FOREIGN KEY (id_album) REFERENCES `album` (id)
 )
"""

table_creation_queries = [MUSICIAN_CREATION, BAND_CREATION, PARTICIPANTS_CREATION, PERFORMER_CREATION, ALBUM_CREATION, SONG_CREATION]
