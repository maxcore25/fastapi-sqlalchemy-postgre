run-db:
    docker run --name test_postgres -p 5432:5432 -e POSTGRESS_PASSWORD=mypassword -e POSTGRES_DB=fastapisqlalchemy -v ${PWD}/db_data\:/var/lib/postgresql/data -d progress