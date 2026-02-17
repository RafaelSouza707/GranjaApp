-- psql -U postgres -d granja_db -f schema.sql


CREATE TABLE IF NOT EXISTS lote_frango (
    id BIGSERIAL PRIMARY KEY,
    quantidade_inicial INTEGER NOT NULL,
    data_entrada_aves DATE NOT NULL,
    data_ninhada DATE,
    fornecedor VARCHAR(100),
    tipo_lote VARCHAR(20),
    galpao INTEGER,
    status VARCHAR(50),
    peso_medio NUMERIC(10,3)
);


CREATE TABLE IF NOT EXISTS lote_racao (
    id BIGSERIAL PRIMARY KEY,
    tipo_racao VARCHAR(30) NOT NULL,
    fornecedor VARCHAR(100),
    data_compra DATE NOT NULL,
    quilos NUMERIC(12,3) NOT NULL,
    valor NUMERIC(15,2) NOT NULL
);


CREATE TABLE IF NOT EXISTS tipo_despesa (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS despesa (
    id BIGSERIAL PRIMARY KEY,
    id_tipo_despesa BIGINT NOT NULL,
    data DATE NOT NULL,
    valor NUMERIC(15,2) NOT NULL,

    CONSTRAINT fk_despesa_tipo
        FOREIGN KEY (id_tipo_despesa)
        REFERENCES tipo_despesa(id)
        ON DELETE RESTRICT
);

CREATE INDEX idx_despesa_tipo ON despesa(id_tipo_despesa);


CREATE TABLE IF NOT EXISTS mortalidade (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    data DATE NOT NULL,
    quantidade_mortes INTEGER NOT NULL,

    CONSTRAINT fk_mortalidade_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_mortalidade_lote ON mortalidade(id_lote_frango);


CREATE TABLE IF NOT EXISTS postura (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    data DATE NOT NULL,
    quantidade_ovos INTEGER NOT NULL,
    ovos_descartados INTEGER NOT NULL,

    CONSTRAINT fk_postura_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE,

    CONSTRAINT unique_postura_dia
        UNIQUE (id_lote_frango, data)
);

CREATE INDEX idx_postura_lote ON postura(id_lote_frango);


CREATE TABLE IF NOT EXISTS corte (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    data DATE NOT NULL,
    peso NUMERIC(12,3) NOT NULL,

    CONSTRAINT fk_corte_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_corte_lote ON corte(id_lote_frango);


CREATE TABLE IF NOT EXISTS venda_corte (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    data DATE NOT NULL,
    valor NUMERIC(15,2) NOT NULL,
    quilos NUMERIC(12,3) NOT NULL,

    CONSTRAINT fk_venda_corte_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE
);

CREATE INDEX  idx_venda_corte_lote ON venda_corte(id_lote_frango);


CREATE TABLE IF NOT EXISTS venda_ovos (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    data DATE NOT NULL,
    valor NUMERIC(15,2) NOT NULL,
    quantidade_ovos INTEGER NOT NULL,

    CONSTRAINT fk_venda_ovos_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_venda_ovos_lote ON venda_ovos(id_lote_frango);

CREATE TABLE IF NOT EXISTS controle_vacinas (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    medicamento_aplicado VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    responsavel_aplicacao VARCHAR(100),

    CONSTRAINT fk_vacina_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_vacina_lote ON controle_vacinas(id_lote_frango);


CREATE TABLE IF NOT EXISTS consumo_lote_diaria (
    id BIGSERIAL PRIMARY KEY,
    id_lote_frango BIGINT NOT NULL,
    id_lote_racao BIGINT NOT NULL,
    data DATE NOT NULL,
    quilos NUMERIC(12,3) NOT NULL,

    CONSTRAINT fk_consumo_lote
        FOREIGN KEY (id_lote_frango)
        REFERENCES lote_frango(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_consumo_racao
        FOREIGN KEY (id_lote_racao)
        REFERENCES lote_racao(id)
        ON DELETE RESTRICT
);

CREATE INDEX idx_consumo_lote ON consumo_lote_diaria(id_lote_frango);
CREATE INDEX idx_consumo_racao ON consumo_lote_diaria(id_lote_racao);