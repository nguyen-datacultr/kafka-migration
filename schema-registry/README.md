helm upgrade \
  schema-registry \
  oci://registry-1.docker.io/bitnamicharts/schema-registry \
  --install \
  --namespace=kafka \
  --create-namespace \
  --values=schema-registry/values.yaml


## References:
https://stackoverflow.com/questions/76157961/how-to-install-confluent-schema-registry-using-bitnami-helm-chart-for-external-k