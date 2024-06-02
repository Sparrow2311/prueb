---Truncar table charges-----
ALTER TABLE companies  DROP CONSTRAINT charges_pk;
truncate charges 
ALTER TABLE companies
ADD CONSTRAINT charges_pk FOREIGN KEY (id) REFERENCES charges(id);
----Truncar table companies -----
truncate companies 
---Truncar table cargo-----
truncate cargo 