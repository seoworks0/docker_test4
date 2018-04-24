#FROM ubuntu:latest

# Build essentials
#RUN apt-get update
#RUN apt-get install -y curl build-essential
#RUN apt-get install -y wget

# Mecab
#RUN wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
#RUN tar zxvf mecab-0.996.tar.gz
#RUN cd mecab-0.996; ./configure --enable-utf8-only; make; make install; ldconfig

# Ipadic
#RUN wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
#RUN tar zxvf mecab-ipadic-2.7.0-20070801.tar.gz
#RUN cd mecab-ipadic-2.7.0-20070801
#RUN ./configure --with-charset=utf8
#RUN make
#RUN make install
#RUN echo "dicdir = /usr/local/lib/mecab/dic/ipadic" > /usr/local/etc/mecabrc

# Clean up
#RUN apt-get remove -y build-essential
#RUN rm -rf mecab-0.996.tar.gz*
#RUN rm -rf mecab-ipadic-2.7.0-20070801*


FROM python:3-alpine
RUN apt-get update && \
    apt-get install -y mecab=0.996-1.1 \
                       libmecab-dev=0.996-1.1 \
                       mecab-ipadic-utf8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install mecab-python==0.996
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
