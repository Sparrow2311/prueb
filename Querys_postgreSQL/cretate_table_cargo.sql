CREATE TABLE public.cargo (
	id varchar(50) NOT NULL,
	company_name varchar(130) NOT NULL,
	company_id varchar(60) NOT NULL,
	amount numeric(16, 2) NOT NULL,
	status varchar(30) NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NOT NULL
);