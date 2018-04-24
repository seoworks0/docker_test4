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

FROM intimatemerger/mecab-python:0.996-alpine
COPY mecabrc /usr/local/etc/mecabrc

RUN apk add --no-cache --virtual=build-deps git bash curl file openssl sudo perl && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd && \
    /tmp/neologd/bin/install-mecab-ipadic-neologd -n -y && \
    apk del build-deps && \
    rm -rf /tmp/neologd

CMD ["/usr/local/bin/mecab"]

FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
