FROM debian:buster-slim
EXPOSE 80

COPY . /var/www/dashboard
WORKDIR /var/www/dashboard

#RUN apt-get update && \
#apt-get install -y libapache2-mod-wsgi-py3 apache2 python3-pip && \
#apt-get clean
#RUN pip3 install -r /var/www/dashboard/requirements.txt

RUN apt-get update && \
apt-get install -y libapache2-mod-wsgi-py3 apache2 python3-ldap3 python3-docker python3-flask python3-requests && \
apt-get clean

RUN mv /var/www/dashboard/apache/dashboard.conf /etc/apache2/sites-enabled/000-default.conf && \
mv /var/www/dashboard/apache/dashboard.wsgi /var/www/dashboard/ && \
rm -rf /var/www/dashboard/apache /var/www/dashboard/docker && \
sed -i 's,ErrorLog .*,ErrorLog /dev/stderr,' /etc/apache2/apache2.conf && \
echo 'TransferLog /dev/stdout' >> /etc/apache2/apache2.conf

CMD apachectl -DFOREGROUND -k start
