exp="35jd"
read -p "num : " num

#for num in {51..100}
#do
python3 controller.py -t "${exp}'s test" -d 13 -f "${exp}.${num}" > "logging/log.${exp}.${num}"
cat "logging/log.${exp}.${num}" |grep "Remote"|grep "ERROR" |cut -d'.' -f 1

# doing remote process of niryo
ssh niryo@192.168.1.187‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && [MY TEST FILE] ’ #cali;do
#done
