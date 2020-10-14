#!/bin/sh
echo "running  initialize_invoicing_db."
initialize_invoicing_db development.ini
echo "Database inicialized ."
echo "start web app"
pserve development.ini 