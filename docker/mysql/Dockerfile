FROM mysql:8.0
RUN usermod -u 1000 mysql
RUN mkdir -p /var/run/mysqld && \
  chmod -R 777 /var/run/mysqld