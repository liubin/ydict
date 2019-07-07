#!/bin/sh

export LANG=zh_CN.utf-8

b=""

while true 
do
  read a
  if [ "$a" != "" ];then
    b=$a
  fi 

  if [ "$b" != "" ];then
    python search.py $b
  fi 

done

