#!/bin/bash
dtime=`date +%Y-%m-%dT%H-%M-%SZ`; 
cd /home/marko/releasespace/
cp -R release-local/ release-local.$dtime; 

zip -r release-local.$dtime.zip release-local.$dtime
gsutil cp release-local.$dtime.zip gs://parquery-releases/production/release-local.$dtime.zip && \
  rm release-local.$dtime.zip && \
  rm -rf release-local.$dtime
