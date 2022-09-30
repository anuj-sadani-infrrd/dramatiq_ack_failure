FROM rabbitmq:3.8.16-management

ENV RABBITMQ_USER test
ENV RABBITMQ_PASSWORD test
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/user/rabbitmq

#COPY ./advanced.config /etc/rabbitmq/advanced.config
COPY ./custom-rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

ADD custom-docker-entrypoint.sh /usr/local/bin
RUN chmod 0755 /usr/local/bin/*.sh

ENTRYPOINT ["custom-docker-entrypoint.sh"]
CMD ["rabbitmq-server"]
