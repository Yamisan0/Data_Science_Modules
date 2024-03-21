docker cp table.sql ex02-db-1:/table.sql
docker exec -it ex02-db-1 psql -U imessaad -d piscineds -f /table.sql
docker cp data_2022_oct.csv ex02-db-1:/data_2022_oct.csv
