
atletas = LOAD '/datalake/jjoo/atletas.csv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','YES_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER') as (atleta:chararray,pais:chararray,deporte:chararray,oro:int,plata:int,bronce:int,total:int);


atletas_limit = LIMIT atletas 10;
DUMP atletas_limit;

