PYTHONPATH=/home/taufer/npfl114/ /home/taufer/.local/bin/ipython notebook --script --port=8228 --profile=sge --no-browser  --ip="`ip a | grep '10\\.10\\.2[45]' | cut -d" "  -f6 | cut -d"/" -f1`"
