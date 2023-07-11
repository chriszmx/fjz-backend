steps = [
    [
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            isAdmin BOOLEAN NOT NULL,
            isTenant BOOLEAN NOT NULL
        );
        """,
        """
        DROP TABLE accounts;
        """
    ]
]
