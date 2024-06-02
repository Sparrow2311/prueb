CREATE TABLE public.companies (
	company_id varchar(60) NOT NULL,
	company_name varchar(130) NULL,
	id varchar(50) NULL
);


-- public.companies foreign keys

ALTER TABLE public.companies ADD CONSTRAINT charges_pk FOREIGN KEY (id) REFERENCES public.charges(id);