How to install mysqlclient in mac

1. brew tap homebrew/core
2. brew install mysql-connector-c
3. brew install pkg-config
4. export MYSQLCLIENT_CFLAGS="-I/usr/local/opt/mysql-client/include/mysql"
5. export MYSQLCLIENT_LDFLAGS="-L/usr/local/opt/mysql-client/lib"
6. pip3 install mysqlclient


How to install mysqlclient in linux or Deb

1. sudo apt-get install libmysqlclient-dev
2. export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
3. export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
4. pip3 install mysqlclient

