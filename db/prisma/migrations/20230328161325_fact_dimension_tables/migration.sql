-- CreateTable
CREATE TABLE "sisu_nota" (
    "id" SERIAL NOT NULL,
    "dimensao_candidato" INTEGER,
    "dimensao_tempo" INTEGER,
    "dimensao_ies" INTEGER,
    "dimensao_campus" INTEGER,
    "dimensao_curso" INTEGER,
    "dimensao_concorrencia" INTEGER,
    "peso_l" DOUBLE PRECISION,
    "peso_ch" DOUBLE PRECISION,
    "peso_cn" DOUBLE PRECISION,
    "peso_m" DOUBLE PRECISION,
    "peso_r" DOUBLE PRECISION,
    "nota_minima_l" DOUBLE PRECISION,
    "nota_minima_ch" DOUBLE PRECISION,
    "nota_minima_cn" DOUBLE PRECISION,
    "nota_minima_m" DOUBLE PRECISION,
    "nota_minima_r" DOUBLE PRECISION,
    "media_minima" DOUBLE PRECISION,
    "nota_l" DOUBLE PRECISION,
    "nota_ch" DOUBLE PRECISION,
    "nota_cn" DOUBLE PRECISION,
    "nota_m" DOUBLE PRECISION,
    "nota_r" DOUBLE PRECISION,
    "nota_l_com_peso" DOUBLE PRECISION,
    "nota_ch_com_peso" DOUBLE PRECISION,
    "nota_cn_com_peso" DOUBLE PRECISION,
    "nota_m_com_peso" DOUBLE PRECISION,
    "nota_r_com_peso" DOUBLE PRECISION,
    "nota_candidato" DOUBLE PRECISION,
    "nota_corte" DOUBLE PRECISION,
    "classificacao" VARCHAR(20),

    CONSTRAINT "sisu_nota_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_candidato" (
    "id" SERIAL NOT NULL,
    "inscrito" VARCHAR(255),
    "sexo" VARCHAR(10),
    "data_nascimento" VARCHAR(12),
    "uf_candidato" VARCHAR(2),
    "municipio_candidato" VARCHAR(255),
    "aprovado" VARCHAR(520),
    "matricula" VARCHAR(50),
    "opcao" VARCHAR(20),

    CONSTRAINT "sisu_candidato_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_tempo" (
    "id" SERIAL NOT NULL,
    "ano" INTEGER,
    "edicao" INTEGER,
    "codigo_etapa" INTEGER,
    "etapa" VARCHAR(50),

    CONSTRAINT "sisu_tempo_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_ies" (
    "id" SERIAL NOT NULL,
    "codigo_ies" INTEGER,
    "nome_ies" VARCHAR(255),
    "sigla_ies" VARCHAR(30),
    "uf_ies" VARCHAR(2),
    "percentual_bonus" DOUBLE PRECISION,

    CONSTRAINT "sisu_ies_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_campus" (
    "id" SERIAL NOT NULL,
    "codigo_campus" INTEGER,
    "nome_campus" VARCHAR(255),
    "uf_campus" VARCHAR(2),
    "municipio_campus" VARCHAR(255),

    CONSTRAINT "sisu_campus_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_curso" (
    "id" SERIAL NOT NULL,
    "codigo_curso" INTEGER,
    "nome_curso" VARCHAR(255),
    "grau" VARCHAR(255),
    "turno" VARCHAR(15),
    "ds_periodicidade" VARCHAR(50),

    CONSTRAINT "sisu_curso_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sisu_concorrencia" (
    "id" SERIAL NOT NULL,
    "tipo_mod_concorrencia" VARCHAR(300),
    "mod_concorrencia" VARCHAR(300),
    "qt_vagas_concorrencia" INTEGER,
    "tp_cota" VARCHAR(300),

    CONSTRAINT "sisu_concorrencia_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "sisu_nota_id_key" ON "sisu_nota"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_candidato_id_key" ON "sisu_candidato"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_tempo_id_key" ON "sisu_tempo"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_ies_id_key" ON "sisu_ies"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_campus_id_key" ON "sisu_campus"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_curso_id_key" ON "sisu_curso"("id");

-- CreateIndex
CREATE UNIQUE INDEX "sisu_concorrencia_id_key" ON "sisu_concorrencia"("id");

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_candidato_fkey" FOREIGN KEY ("dimensao_candidato") REFERENCES "sisu_candidato"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_tempo_fkey" FOREIGN KEY ("dimensao_tempo") REFERENCES "sisu_tempo"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_ies_fkey" FOREIGN KEY ("dimensao_ies") REFERENCES "sisu_ies"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_campus_fkey" FOREIGN KEY ("dimensao_campus") REFERENCES "sisu_campus"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_curso_fkey" FOREIGN KEY ("dimensao_curso") REFERENCES "sisu_curso"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_concorrencia_fkey" FOREIGN KEY ("dimensao_concorrencia") REFERENCES "sisu_concorrencia"("id") ON DELETE SET NULL ON UPDATE CASCADE;
