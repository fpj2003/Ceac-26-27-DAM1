CREATE USER 'examendamceac2627'@'localhost' IDENTIFIED BY 'CEACExamenDAM123$';
@ = at (en)


GRANT USAGE ON *.* TO 'examendamceac2627'@'localhost';



ALTER USER 'examendamceac2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;



GRANT ALL PRIVILEGES ON examendamceac2627.* 
TO 'examendamceac2627'@'localhost';

FLUSH PRIVILEGES;
