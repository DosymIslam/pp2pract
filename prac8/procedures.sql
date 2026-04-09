CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE name = p_name
          AND surname = p_surname
    ) THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name
          AND surname = p_surname;

    ELSE

        INSERT INTO contacts(name, surname, phone)
        VALUES (p_name, p_surname, p_phone);

    END IF;

END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    names TEXT[],
    surnames TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN

    invalid_data := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(names, 1)
    LOOP

        IF phones[i] ~ '^[0-9]{11}$' THEN

            INSERT INTO contacts(name, surname, phone)
            VALUES (
                names[i],
                surnames[i],
                phones[i]
            );

        ELSE

            invalid_data := array_append(
                invalid_data,
                phones[i]
            );

        END IF;

    END LOOP;

END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM contacts
    WHERE name = p_value
       OR surname = p_value
       OR phone = p_value;

END;
$$;