CREATE TABLE IF NOT EXISTS substitut (
    id_substitut SMALLINT AUTO_INCREMENT NOT NULL,
    id_substitut_of SMALLINT NOT NULL,
    PRIMARY KEY (id_substitut),
    CONSTRAINT fk_substit_aliment FOREIGN KEY(id_substitut) REFERENCES Aliment(id_aliment)
    ON UPDATE CASCADE,
    CONSTRAINT fk_substit_aliment_of FOREIGN KEY(id_substitut_of) REFERENCES Aliment(id_aliment) ON UPDATE CASCADE

)
Engine = InnoDB;