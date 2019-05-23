CREATE TABLE Aliment (
    barecode VARCHAR(15) NOT NULL,
    name_aliment VARCHAR(150) NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    store VARCHAR(50),
    grade CHAR(1) NOT NULL,
    link TEXT,
    substitut VARCHAR(15)  ,
    PRIMARY KEY (barecode),
    CONSTRAINT fk_category FOREIGN KEY(category) REFERENCES Category(id_category),
    CONSTRAINT fk_subsitut FOREIGN KEY(substitut) REFERENCES Aliment(barecode)
)
ENGINE = InnoDB;