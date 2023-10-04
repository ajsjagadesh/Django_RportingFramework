SERVICE_PORT=9090

echo  -e "\033[1;32m`date`:\tStarting Service\033[0m"
(ENV=${ENV} LOG=${LOG} python3 manage.py runserver 0.0.0.0:${SERVICE_PORT} )
echo -e "\033[1;32m`date`:\tService started with LOG LEVEL ${LOG}..... \n"