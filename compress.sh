#!/bin/bash

D="fa/jquery/jquery-ui-1.7.2.custom";
CMD="python compressor.py  -c $HOME/jar/yuicompressor-2.4.2.jar "
$CMD -o $D/fa.jquery.min.css -t css $(find $D  -mindepth 2 -maxdepth 2 -name "*.css")
$CMD -o $D/fa.jquery.min.js $(find $D/js -name "*.js") $(find $D/co* -name "*.js")