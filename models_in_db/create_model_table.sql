DROP TABLE IF EXISTS futurex_model_catalog;
CREATE TABLE futurex_model_catalog
(
    model_id integer NOT NULL,
    model_name character varying COLLATE pg_catalog."default" NOT NULL,
    model_file bytea NOT NULL
);