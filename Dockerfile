FROM python:3

RUN curl -sL https://github.com/XAMPPRocky/tokei/releases/download/v10.0.1/tokei-v10.0.1-x86_64-unknown-linux-musl.tar.gz \
  | tar xvzf - -C /usr/local/bin

COPY . .

RUN make
