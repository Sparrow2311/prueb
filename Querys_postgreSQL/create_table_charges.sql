CREATE TABLE public.charges (
	id varchar(50) NOT NULL,
	amount numeric(16, 2) NOT NULL,
	status varchar(30) NOT NULL,
	created_at timestamp NOT NULL,
	paid_at timestamp NOT NULL,
	CONSTRAINT charges_pk PRIMARY KEY (id)
);