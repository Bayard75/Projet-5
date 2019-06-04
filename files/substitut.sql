CREATE TABLE IF NOT EXISTS substitut (
    id_substitut SMALLINT AUTO_INCREMENT NOT NULL,
    id_substitut_of SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_substitut),
    CONSTRAINT fk_substit_cat FOREIGN KEY(id_substitut) REFERENCES Aliment(id_aliment)
    ON UPDATE CASCADE

)
Engine = InnoDB;