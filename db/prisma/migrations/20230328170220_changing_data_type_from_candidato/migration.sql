/*
  Warnings:

  - The `data_nascimento` column on the `sisu_candidato` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `opcao` column on the `sisu_candidato` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - Added the required column `aprovado` to the `sisu_candidato` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "sisu_candidato" DROP COLUMN "data_nascimento",
ADD COLUMN     "data_nascimento" DATE,
DROP COLUMN "aprovado",
ADD COLUMN     "aprovado" BOOLEAN NOT NULL,
DROP COLUMN "opcao",
ADD COLUMN     "opcao" INTEGER;
