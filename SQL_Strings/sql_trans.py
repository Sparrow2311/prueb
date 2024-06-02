class transfor:

    QUERY_TRANS = """

        INSERT INTO public.cargo
        (id, company_name, company_id, amount, status, created_at, updated_at)
        VALUES('{}', '{}', '{}', {}, '{}', '{}', '{}');

    """