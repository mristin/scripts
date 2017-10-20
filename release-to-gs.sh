#!/bin/bash
rm -rf /home/marko/releasespace/build-local
rm -rf /home/marko/releasespace/release-local
bld.sh

dtime=`date -u +%Y-%m-%dT%H-%M-%SZ`; 
cd /home/marko/releasespace/
cp -R release/ release.$dtime; 

zip -r release.$dtime.zip release.$dtime
gsutil cp release.$dtime.zip gs://parquery-releases/production/release.$dtime.zip && \
  rm release.$dtime.zip && \
  rm -rf release.$dtime
