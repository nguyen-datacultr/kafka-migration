name=$1
action=$2
echo "Creating pv and storage..."
kubectl $2 -f /home/ubuntu/kafka-pipline/storage/pv-$1.yaml
kubectl $2 -f /home/ubuntu/kafka-pipline/storage/sc-$1.yaml