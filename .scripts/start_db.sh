#!/usr/bin/env bash

docker-compose up -d database

sleep 10

mysql -h 127.0.0.1 -u root -p1234 -P3306 < .sql/nidus_database_core_v2.sql
