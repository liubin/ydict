#!/bin/sh

export LANG=zh_CN.utf-8

b=""

while true 
do
  read a
  if [ "$a" != "" ];then
    b=$a
  fi 

  python search.py $b
done

