helm repo add redpanda https://charts.redpanda.com
helm upgrade --install redpanda-controller redpanda/operator \
  --namespace kafka \
  --set image.repository=docker.redpanda.com/redpandadata/redpanda-operator \
  --set image.tag=v23.2.11 \
  --create-namespace


---
https://charts.kpow.io/
