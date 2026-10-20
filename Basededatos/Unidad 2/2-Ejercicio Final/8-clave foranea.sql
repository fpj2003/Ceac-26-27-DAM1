ALTER TABLE jugadores
ADD CONSTRAINT fk_club_jugador FOREIGN KEY (id_club) REFERENCES club(id_club);