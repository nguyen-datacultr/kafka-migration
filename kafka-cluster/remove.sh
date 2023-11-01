echo "Delete kafka"
kubectl delete -f ./kafka.yaml

echo "Delete pvc"
kubectl delete pvc data-demo-zookeeper-0
kubectl delete pvc data-demo-zookeeper-1
kubectl delete pvc data-demo-zookeeper-2

echo "Delete pv and sc"
sh ./storage/storage-apply.sh delete

echo "Restart pv and sc"
sh ./storage/storage-apply.sh apply
