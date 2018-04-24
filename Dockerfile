FROM debian:stable-slim

# Moving on...
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y git build-essential make unrar-free autoconf \
	automake libtool gcc g++ gperf flex bison texinfo gawk ncurses-dev \
	libexpat-dev python-dev python python-serial sed unzip bash help2man \
	wget bzip2 libtool-bin
RUN useradd build
RUN mkdir -p /data ; chown -R build /data

USER build
WORKDIR /data
RUN git clone --recursive https://github.com/pfalcon/esp-open-sdk
RUN git clone --recursive https://github.com/jpvlsmv/micropython-tweaks /data/micropython

WORKDIR /data/esp-open-sdk
RUN make
ENV PATH="/data/esp-open-sdk/xtensa-lx106-elf/bin:$PATH"

WORKDIR /data/micropython/ 
RUN git submodule update --init
RUN git merge --theirs /data/micropython-tweaks
RUN make -C mpy-cross

WORKDIR /data/micropython/ports/esp8266
RUN make axtls && make 

COPY docker-interactive-entry.sh /usr/bin/
ENTRYPOINT ["/usr/bin/docker-interactive-entry.sh"]
CMD ["bash"]
