for i in {22..100}
do
    count="collision${i}.csv"
    python controller.py -t test -d 11 -f "${count}"
done
