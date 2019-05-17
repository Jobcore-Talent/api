FROM gitpod/workspace-postgres

USER root

RUN postgres -V \
  && apt-get -y remove --purge postgresql-10 \
  && apt-get -y install postgresql-10
