-- Check if the 'hbnb_test_db' database exists
SELECT IF(EXISTS (SELECT 1 FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'test_db'), 'Database exists', 'Database does not exist') AS Result;

-- Check if the 'hbnb_test' user exists
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'hbnb_test' AND host = 'localhost'), 'User exists', 'User does not exist') AS Result;

-- Check if 'hbnb_test' user has privileges on 'test_db' and 'performance_schema'
SELECT IF(EXISTS (SELECT 1 FROM information_schema.SCHEMA_PRIVILEGES WHERE GRANTEE = 'hbnb_test@localhost' AND TABLE_SCHEMA = 'test_db' AND PRIVILEGE_TYPE = 'ALL PRIVILEGES'), 'User has privileges on test_db', 'User does not have privileges on test_db') AS Result;

SELECT IF(EXISTS (SELECT 1 FROM information_schema.SCHEMA_PRIVILEGES WHERE GRANTEE = 'hbnb_test@localhost' AND TABLE_SCHEMA = 'performance_schema' AND PRIVILEGE_TYPE = 'SELECT'), 'User has SELECT privileges on performance_schema', 'User does not have SELECT privileges on performance_schema') AS Result;
