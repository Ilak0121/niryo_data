exp="35jd"
read -p "num : " num

#for num in {51..100}
#do
python3 controller.py -t "${exp}'s test" -d 13 -f "${exp}.${num}" > "logging/log.${exp}.${num}"
cat "logging/log.${exp}.${num}" |grep "Remote"|grep "ERROR" |cut -d'.' -f 1
#done
