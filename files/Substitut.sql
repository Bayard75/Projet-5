CREATE TABLE IF NOT EXISTS Sub(
    id_sub SMALLINT NOT NULL,
    is_sub_of VARCHAR(150),
    CONSTRAINT fk_id_sub FOREIGN KEY(id_sub) REFERENCES Aliment(id_aliment),
    CONSTRAINT fk_is_sub_of FOREIGN KEY(is_sub_of) REFERENCES Aliment(name_aliment),
    UNIQUE INDEX (id_sub, is_sub_of)
)
ENGINE = InnoDB;