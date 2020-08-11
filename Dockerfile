FROM python:3.6

RUN apt-get update && apt-get install -y \
    mercurial \
    ffmpeg \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libplib-dev \
    libopenal-dev \
    libalut-dev \
    libvorbis-dev \
    libxxf86vm-dev \
    libxmu-dev \
    libgl1-mesa-dev \
    git

RUN apt-get install -qqy x11-apps

WORKDIR /app
COPY . .

RUN python3 setup.py install