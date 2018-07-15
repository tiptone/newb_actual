FROM debian:latest
#FROM tensorflow/tensorflow:latest


RUN apt-get update && apt-get install -y \
    git \
    openssh-server \
    python3

#RUN echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config
RUN mkdir ~/.ssh && ln -s /run/secrets/host_ssh_key ~/.ssh/id_rsa

#RUN python3 -m ensurepip

#RUN pip install -r ../../skeefooza/requirements.txt

#COPY ./skeefooza/hello_world.py /tmp

#CMD python /app/app.py
