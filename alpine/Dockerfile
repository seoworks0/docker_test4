FROM python:3-alpine

ADD mecab-0.996.tar.gz /tmp

RUN apk add --no-cache build-base && \
    cd /tmp/mecab-0.996 && \
        ./configure && \
        make && \
        make check && \
        make install && \
    cd / && \
    rm -rf /tmp/mecab-0.996 && \
    pip install mecab-python==0.996
