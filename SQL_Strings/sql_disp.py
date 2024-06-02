class DISPE:

 QUERY_INSERT_CS = """
 
    INSERT INTO public.charges
            (id, amount, status, created_at, paid_at)
            VALUES('{}', {}, '{}', '{}', '{}');

    """
 
 QUERY_INSERT_CY = """
 
    INSERT INTO public.companies
                (company_id, company_name, id)
                VALUES('{}', '{}', '{}');

    """