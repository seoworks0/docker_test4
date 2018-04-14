FROM python:3-alpine
ENV PYTHONUNBUFFERED 1 noninteractive
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install wget g++ make golang mercurial

RUN cd /root; wget https://mecab.googlecode.com/files/mecab-0.996.tar.gz
RUN cd /root; wget https://mecab.googlecode.com/files/mecab-ipadic-2.7.0-20070801.tar.gz

RUN mkdir -p /root/go/src
RUN mkdir -p /root/go/bin
ENV GOPATH /root/go
ENV PATH $PATH:/root/go/bin

# --- mecab install
RUN cd /root; \
    tar xvf mecab-0.996.tar.gz; \
    cd /root/mecab-0.996; \
    ./configure --enable-utf8-only; \
    make; \
    make install

RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/mecab
RUN ldconfig

# --- mecab dic
RUN cd /root; \
   tar xvf mecab-ipadic-2.7.0-20070801.tar.gz

RUN cd /root/mecab-ipadic-2.7.0-20070801; \
    ./configure --with-charset=utf8; \
    make; \
    make install
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
