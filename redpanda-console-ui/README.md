helm repo add redpanda 'https://charts.redpanda.com/' 
helm repo update
kubectl kustomize https://github.com/redpanda-data/redpanda/src/go/k8s/config/crd | kubectl apply -f -
helm upgrade \
    redpanda-console-demo \
    redpanda/console \
    --install \
    --namespace=kafka \
    --create-namespace \
    --values=redpanda-console-ui/values.yaml
