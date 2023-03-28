/*
  Warnings:

  - Made the column `dimensao_candidato` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.
  - Made the column `dimensao_tempo` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.
  - Made the column `dimensao_ies` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.
  - Made the column `dimensao_campus` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.
  - Made the column `dimensao_curso` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.
  - Made the column `dimensao_concorrencia` on table `sisu_nota` required. This step will fail if there are existing NULL values in that column.

*/
-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_campus_fkey";

-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_candidato_fkey";

-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_concorrencia_fkey";

-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_curso_fkey";

-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_ies_fkey";

-- DropForeignKey
ALTER TABLE "sisu_nota" DROP CONSTRAINT "sisu_nota_dimensao_tempo_fkey";

-- AlterTable
ALTER TABLE "sisu_nota" ALTER COLUMN "dimensao_candidato" SET NOT NULL,
ALTER COLUMN "dimensao_tempo" SET NOT NULL,
ALTER COLUMN "dimensao_ies" SET NOT NULL,
ALTER COLUMN "dimensao_campus" SET NOT NULL,
ALTER COLUMN "dimensao_curso" SET NOT NULL,
ALTER COLUMN "dimensao_concorrencia" SET NOT NULL;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_candidato_fkey" FOREIGN KEY ("dimensao_candidato") REFERENCES "sisu_candidato"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_tempo_fkey" FOREIGN KEY ("dimensao_tempo") REFERENCES "sisu_tempo"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_ies_fkey" FOREIGN KEY ("dimensao_ies") REFERENCES "sisu_ies"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_campus_fkey" FOREIGN KEY ("dimensao_campus") REFERENCES "sisu_campus"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_curso_fkey" FOREIGN KEY ("dimensao_curso") REFERENCES "sisu_curso"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "sisu_nota" ADD CONSTRAINT "sisu_nota_dimensao_concorrencia_fkey" FOREIGN KEY ("dimensao_concorrencia") REFERENCES "sisu_concorrencia"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
